"""Quiz cog: /jq start + progression commands + idle watcher.

discord.py 2.7.1, see docs/discord-py/ (Cog, app_commands.Group,
tasks.loop, View/Select for the badge loadout UI).
Implements views.QuizHooks (db + progression live behind button presses).
"""

from __future__ import annotations

import datetime as dt
import io
import logging
import time

import discord
import yaml
from discord import app_commands
from discord.ext import commands, tasks

from . import badges as badge_engine
from . import embeds, progression
from .config import Settings
from .db import Database, season_exp_from_file
from .models import QuizConfig
from .quiz import QuizManager, QuizSession
from .render import BANNERS, RANK_FILES, badge_icon, profile_card
from .store import ALL_LEVELS, QuestionStore
from .views import QuizView, SetupView

log = logging.getLogger("jlpt_bot.cog")


def _display_name(user: object) -> str:
    return getattr(user, "display_name", None) or getattr(user, "name", "player")


class BadgeView(discord.ui.View):
    """Equip/unequip loadout UI (ephemeral). Rebuilt fresh after each change."""

    def __init__(self, cog: QuizCog, user_id: int, owned: list[dict], name_map: dict[str, dict]):
        super().__init__(timeout=180)
        self.cog = cog
        self.user_id = user_id
        equip_opts = [
            discord.SelectOption(label=f"{name_map[o['badge_id']]['en']} ({name_map[o['badge_id']]['rarity']})",
                                 value=o["badge_id"])
            for o in owned if not o["equipped"]
        ][:25]
        unequip_opts = [
            discord.SelectOption(label=f"{name_map[o['badge_id']]['en']}", value=o["badge_id"])
            for o in owned if o["equipped"]
        ][:25]
        if equip_opts:
            sel = discord.ui.Select(placeholder="Equip a badge (max 8 shown)", options=equip_opts,
                                    min_values=1, max_values=1)
            sel.callback = self._equip  # type: ignore[method-assign]
            self.add_item(sel)
        if unequip_opts:
            sel2 = discord.ui.Select(placeholder="Unequip a badge", options=unequip_opts,
                                     min_values=1, max_values=1)
            sel2.callback = self._unequip  # type: ignore[method-assign]
            self.add_item(sel2)

    async def _refresh(self, interaction: discord.Interaction, note: str) -> None:
        owned = await self.cog.db.owned_badges(self.user_id)
        equipped = [o for o in owned if o["equipped"]]
        desc = "Shown on your card:\n" + (
            "\n".join(f"• {self.cog.badge_map[o['badge_id']]['en']}" for o in equipped) or "(none)") + f"\n\n{note}"
        await interaction.response.edit_message(
            content=desc, view=BadgeView(self.cog, self.user_id, owned, self.cog.badge_map))

    async def _equip(self, interaction: discord.Interaction) -> None:
        select = next(c for c in self.children if isinstance(c, discord.ui.Select)
                      and c.placeholder.startswith("Equip"))
        ok = await self.cog.db.set_equipped(self.user_id, select.values[0], True)
        await self._refresh(interaction, "Equipped." if ok else "Slots full (8/8) — unequip one first.")

    async def _unequip(self, interaction: discord.Interaction) -> None:
        select = next(c for c in self.children if isinstance(c, discord.ui.Select)
                      and c.placeholder.startswith("Unequip"))
        await self.cog.db.set_equipped(self.user_id, select.values[0], False)
        await self._refresh(interaction, "Unequipped.")


class QuizCog(commands.Cog):
    def __init__(self, bot: commands.Bot, settings: Settings, store: QuestionStore,
                 manager: QuizManager, db: Database, prog: dict):
        self.bot = bot
        self.settings = settings
        self.store = store
        self.manager = manager
        self.db = db
        self.exp_cfg: dict = prog.get("exp", {})
        self.ranks_cfg: list[dict] = prog.get("ranks", [])
        self.badges_cfg: list[dict] = prog.get("badges", [])
        self.badge_map = {b["id"]: b for b in self.badges_cfg}
        self.season_months = int(prog.get("season", {}).get("months", 2))
        self.season: dict = {"id": 1, "started_ts": 0.0, "ends_ts": 0.0}
        self.rank_index = {r["id"]: i for i, r in enumerate(self.ranks_cfg)}
        self.idle_watcher.start()

    def cog_unload(self) -> None:
        self.idle_watcher.cancel()

    # ---------- season ----------

    async def ensure_season(self) -> dict:
        self.season = await self.db.ensure_season(self.season_months)
        return self.season

    def days_left(self) -> int:
        return max(0, int((self.season.get("ends_ts", 0) - time.time()) / 86400))

    def lifetime_exp(self, user_id: int, season_exp: int) -> int:
        archived = []
        for path in sorted(self.db.archive_dir.glob("quiz-season-*.db")):
            archived.append(season_exp_from_file(path).get(user_id, 0))
        return progression.lifetime_exp(season_exp, archived, int(self.exp_cfg.get("lifetime_ceiling", 1_000_000)))

    # ---------- QuizHooks ----------

    async def on_session_start(self, session: QuizSession) -> None:
        await self.ensure_season()
        await self.db.upsert_player(session.config.starter_id, session.config.starter_name)
        await self.db.start_session_row(session.tag, self.season["id"], session.total)

    async def _refresh_rank(self, user_id: int) -> str | None:
        stats = await self.db.get_stats(user_id)
        per_lvl = {lvl: v.get("c", 0) for lvl, v in (stats.get("per_level") or {}).items()}
        recent = await self.db.recent_answers(user_id, 100)
        idx = progression.rank_index_for(
            int(stats.get("exp", 0)), per_lvl, self.ranks_cfg, recent,
            int(stats.get("wins", 0)), int(stats.get("best_n1_streak", 0)))
        new_id = self.ranks_cfg[idx]["id"]
        if self.rank_index.get(stats.get("rank_id", "houga"), 0) < idx:
            await self.db.set_rank(user_id, new_id)
            return str(new_id)
        return None

    async def _check_badges(self, user_id: int, event: dict | None = None) -> list[str]:
        stats = await self.db.get_stats(user_id)
        recent = await self.db.recent_answers(user_id, 100)
        snapshot = {
            "first_bloods": stats.get("first_bloods", 0),
            "best_streak": stats.get("best_streak", 0),
            "mistakes": stats.get("mistakes", 0),
            "clean_sessions": stats.get("clean_sessions", 0),
            "wins": stats.get("wins", 0),
            "giant_slays": stats.get("giant_slays", 0),
        }
        fresh = []
        for bid in badge_engine.check_badges(self.badges_cfg, snapshot, recent, event):
            if await self.db.award_badge(user_id, bid):
                fresh.append(bid)
        return fresh

    def _rank_name(self, rank_id: str) -> str:
        for r in self.ranks_cfg:
            if r["id"] == rank_id:
                return f"{r['en']} {r.get('ja', '')}".strip()
        return rank_id

    async def on_scoring_press(self, *, user_id: int, name: str, level: str, correct: bool,
                               ms: int, hour: int, session_tag: str, channel: object) -> None:
        await self.ensure_season()
        await self.db.upsert_player(user_id, name)
        day = Database.today_day()
        stats = await self.db.record_answer(
            user_id, self.season["id"], level, correct, ms if correct else None, session_tag, day, hour)
        event: dict = {"hour": hour}
        if not correct:
            await self._check_badges(user_id, event)
            return
        await self.db.mark_first_blood(user_id)
        streak_after = int(stats.get("cur_streak", 1))
        exp, _bonuses = progression.answer_exp(
            level, ms / 1000.0, streak_after, int(stats.get("correct_today", 1)) - 1,
            progression.is_weekend(), self.exp_cfg)
        if stats.get("first_today"):
            exp += int(self.exp_cfg.get("daily_first_answer", {}).get("flat", 50))
            if hour < 10:
                event["early_bird"] = True
        if 0 <= hour < 4:
            event["night_owl"] = True
        await self.db.add_exp(user_id, exp)
        fresh = await self._check_badges(user_id, event)
        new_rank = await self._refresh_rank(user_id)
        notes = []
        if new_rank:
            notes.append(f"🎖 {name} Rank UP → **{self._rank_name(new_rank)}**!")
        for bid in fresh:
            b = self.badge_map.get(bid, {})
            notes.append(f"🏅 {name} earned **{b.get('en', bid)}**!")
        if notes:
            try:
                await channel.send("\n".join(notes))  # type: ignore[attr-defined]
            except Exception:
                log.exception("rank-up announce failed")

    async def on_session_end(self, session: QuizSession, reason: str) -> str:
        await self.ensure_season()
        winner = session.winner()
        winner_id = winner.user_id if winner else None
        notes: list[str] = []
        if winner is not None:
            mistakes = session.session_mistakes.get(winner_id or 0, 0)
            is_clean = mistakes == 0
            is_comeback = (session.half_leader_id is not None
                           and session.half_leader_id != winner_id)
            opp_best = -1
            for uid in session.participants:
                if uid == winner_id:
                    continue
                st = await self.db.get_stats(uid)
                opp_best = max(opp_best, self.rank_index.get(st.get("rank_id", "houga"), 0))
            wstats = await self.db.get_stats(winner_id or 0)
            is_giant = opp_best > self.rank_index.get(wstats.get("rank_id", "houga"), 0)
            if reason == "finished":
                if is_clean:
                    await self.db.record_clean_session(winner_id or 0)
                bonus, bnames = progression.session_win_exp(is_clean, is_comeback, is_giant, self.exp_cfg)
                if bonus:
                    await self.db.add_exp(winner_id or 0, bonus)
                    notes.append(f"✨ +{bonus} EXP ({', '.join(bnames)})")
                if is_giant:
                    await self.db.record_giant_slay(winner_id or 0)
            await self.db.record_session_end(
                session.tag, self.season["id"], winner_id, session.half_leader_id, session.total)
            for uid in session.participants:
                fresh = await self._check_badges(uid)
                nm = await self._player_name(uid)
                for bid in fresh:
                    notes.append(f"🏅 {nm} earned **{self.badge_map.get(bid, {}).get('en', bid)}**!")
                new_rank = await self._refresh_rank(uid)
                if new_rank:
                    notes.append(f"🎖 {nm} Rank UP → **{self._rank_name(new_rank)}**!")
        else:
            await self.db.record_session_end(
                session.tag, self.season["id"], None, session.half_leader_id, session.total)
        return "\n".join(notes)

    async def _player_name(self, user_id: int) -> str:
        async with self.db._lock:
            assert self.db._db is not None
            cur = await self.db._db.execute("SELECT name FROM players WHERE user_id=?", (user_id,))
            row = await cur.fetchone()
            return str(row[0]) if row else f"<@{user_id}>"

    # ---------- slash commands ----------

    jq = app_commands.Group(name="jq", description="JLPT quiz commands")

    def _guarded(self, interaction: discord.Interaction) -> bool:
        return (interaction.guild_id == self.settings.guild_id
                and interaction.channel_id == self.settings.channel_id)

    @jq.command(name="start", description="Start a JLPT quiz setup")
    async def jq_start(self, interaction: discord.Interaction) -> None:
        if not self._guarded(interaction):
            await interaction.response.send_message(embed=embeds.guard_embed(), ephemeral=True)
            return
        existing = await self.manager.get()
        if existing is not None:
            await interaction.response.send_message(embed=embeds.busy_embed(), ephemeral=True)
            return
        view = SetupView(store=self.store, manager=self.manager, settings=self.settings, hooks=self)
        await interaction.response.send_message(embed=embeds.setup_embed(), view=view, ephemeral=True)
        log.info("setup opened by %s (%s)", interaction.user, interaction.user.id)

    async def _profile_payload(self, user_id: int, name: str, avatar: bytes | None) -> dict | None:
        stats = await self.db.get_stats(user_id)
        if int(stats.get("answers", 0)) == 0 and not await self.db.owned_badges(user_id):
            return None
        rank_id = str(stats.get("rank_id", "houga"))
        rank_idx = self.rank_index.get(rank_id, 0)
        rank_cfg = self.ranks_cfg[rank_idx]
        special = rank_idx >= 4
        per = stats.get("per_level") or {}
        answers = int(stats.get("answers", 0))
        correct = int(stats.get("correct", 0))
        mistakes = int(stats.get("mistakes", 0))
        acc = round(100 * correct / answers, 1) if answers else 0.0
        resp_c = int(stats.get("resp_count", 0))
        avg_s = round(int(stats.get("resp_ms_total", 0)) / resp_c / 1000, 1) if resp_c else 0.0
        fast = int(stats.get("fastest_ms") or 0) / 1000 if stats.get("fastest_ms") else 0.0
        sessions = await self.db.sessions_played(user_id)
        stat_list = [
            ("Accuracy", acc), ("Answers", answers), ("Correct", correct), ("Mistakes", mistakes),
            ("Avg speed", avg_s), ("Fastest", fast), ("Best streak", int(stats.get("best_streak", 0))),
            ("Sessions", sessions), ("Wins", int(stats.get("wins", 0))),
            ("First bloods", int(stats.get("first_bloods", 0))),
            ("Clean", int(stats.get("clean_sessions", 0))), ("Comebacks", int(stats.get("comebacks", 0))),
        ]
        levels = [(lvl, per.get(lvl, {}).get("c", 0)) for lvl in ["N5", "N4", "N3", "N2", "N1"]]
        owned = await self.db.owned_badges(user_id)
        equipped = [o for o in owned if o["equipped"]][:8]
        theme = rank_id if special else ""
        badge_items = []
        for o in equipped:
            b = self.badge_map.get(o["badge_id"], {})
            base = str(b.get("icon", "drop"))
            badge_items.append({
                "icon": badge_icon(o["badge_id"], base, str(b.get("rarity", "common")),
                                   False, theme, self.assets_dir()),
                "name": str(b.get("en", o["badge_id"])),
                "rarity": str(b.get("rarity", "common")), "locked": False})
        exp = int(stats.get("exp", 0))
        nxt = self.ranks_cfg[rank_idx + 1] if rank_idx + 1 < len(self.ranks_cfg) else None
        if rank_idx >= len(self.ranks_cfg) - 1:
            xp_max, xp_pct, xp_next = None, 100, None
        else:
            assert nxt is not None
            lo, hi = int(rank_cfg.get("threshold", 0)), int(nxt.get("threshold", 1))
            xp_max, xp_pct = hi, round(100 * (exp - lo) / max(1, hi - lo))
            xp_next = f"{nxt['en']} {nxt.get('ja', '')}".strip()
        title = rank_cfg["en"]
        if equipped:
            order = {"legendary": 3, "epic": 2, "rare": 1, "common": 0}
            top = max(equipped, key=lambda o: order.get(self.badge_map.get(o["badge_id"], {}).get("rarity", "common"), 0))
            title = str(self.badge_map.get(top["badge_id"], {}).get("en", title))
        return {
            "theme": "special" if special else "normal",
            "rank": {"id": rank_id, "en": str(rank_cfg["en"]), "ja": str(rank_cfg.get("ja", "")),
                     "index": rank_idx, "icon": RANK_FILES[rank_idx]},
            "name": name, "initial": (name[:1] or "?").upper(), "title": title,
            "avatar_bytes": avatar, "xp_cur": exp, "xp_max": xp_max, "xp_pct": max(0, min(100, xp_pct)),
            "xp_next": xp_next, "stats": stat_list, "levels": levels, "badges": badge_items,
            "badges_earned": len(owned), "badges_total": len(self.badges_cfg),
            "season_id": self.season.get("id", 1), "days_left": self.days_left(),
            "streak": int(stats.get("day_streak", 0)),
            "lifetime": self.lifetime_exp(user_id, exp),
            "css_vars": self._theme_vars(rank_id),
            "banner": BANNERS.get(rank_id), "stars": self._stars(),
            "page_size": "1280px 980px" if special else "1280px 720px",
        }

    def assets_dir(self):  # type: ignore[no-untyped-def]
        from pathlib import Path
        return Path(__file__).parent / "assets"

    def _theme_vars(self, rank_id: str) -> str:
        base = {
            "meijin": ("--acc:#C9A227; --acc2:#E8C86A; --trim:#C9A227; --tt:#FFFFFF; "
                       "--bg:#100D08; --pill:#1E1811; --pline:#3D3423; --bline:#4A3D24; --track:#2B241A; "
                       "--ink:#FFFFFF; --muted:#9AA3C0; --sub:#C9D1E8; --foot:#6B7494; "
                       "--tsh:rgba(0,0,0,0.9); --locked:#171208; --lockedline:#3A3122; --lockedtxt:#8A7F68; "
                       "--nmc:#FFFFFF; --barbg:rgba(255,255,255,0.25);"),
            "shindan": ("--acc:#B98A12; --acc2:#E8C86A; --trim:#B98A12; --tt:#5A3D0C; --nmc:#3A2A10; "
                        "--tsh:rgba(255,255,255,0.9); --bg:#FAF3E2; --pill:#FFFFFF; --pline:#E4C87E; "
                        "--bline:#D9B45F; --track:#EFE0BC; --ink:#3A2A10; --muted:#8A7A52; --sub:#6B5D3A; "
                        "--foot:#8A7A52; --locked:#F1E9D2; --lockedline:#D8C89A; --lockedtxt:#A89878; "
                        "--barbg:rgba(58,42,16,0.18);"),
        }
        if rank_id in base:
            return base[rank_id]
        color = next((r.get("color", "#8A94A6") for r in self.ranks_cfg if r["id"] == rank_id), "#8A94A6")
        return (f"--acc:{color}; --acc2:{color}; --trim:#F5C542; --tt:#F5C542; "
                "--bg:#0A1130; --pill:#161D45; --pline:#2C3768; --bline:#3A4678; --track:#232C5C; "
                "--ink:#FFFFFF; --muted:#9AA3C0; --sub:#C9D1E8; --foot:#6B7494; "
                "--tsh:rgba(0,0,0,0.9); --locked:#12173A; --lockedline:#2A3260; --lockedtxt:#6B7494; "
                "--nmc:#FFFFFF; --barbg:rgba(255,255,255,0.25); --deep:#0A1130;")

    def _normal_vars(self, rank_id: str) -> str:
        color = next((r.get("color", "#8A94A6") for r in self.ranks_cfg if r["id"] == rank_id), "#8A94A6")
        deep = {"houga": "#3E7A32", "reimei": "#A5660F", "saku": "#A63A60", "seikou": "#2F6489"}.get(rank_id, "#2E3440")
        return f"--acc:{color}; --deep:{deep}"

    @staticmethod
    def _stars() -> str:
        return "".join(
            f'<span style="left:{x}%;top:{y}%;font-size:{s}px;">★</span>'
            for x, y, s in [(6, 22, 26), (14, 64, 16), (55, 70, 24), (70, 20, 15), (93, 18, 16)])

    async def _send_profile(self, interaction: discord.Interaction, user: object, ephemeral: bool = False) -> None:
        await interaction.response.defer(ephemeral=ephemeral)
        uid = int(getattr(user, "id", 0))
        name = _display_name(user)
        avatar = None
        try:
            asset = getattr(user, "display_avatar", None)
            if asset is not None:
                avatar = await asset.read()
        except Exception:
            avatar = None
        await self.db.upsert_player(uid, name)
        payload = await self._profile_payload(uid, name, avatar)
        if payload is None:
            await interaction.followup.send("No record yet — play a quiz first!", ephemeral=True)
            return
        from .render import profile_card as render_card
        if payload["theme"] == "normal":
            payload["css_vars"] = self._normal_vars(payload["rank"]["id"])
        png = await self.bot.loop.run_in_executor(
            None, render_card, payload, str(self.assets_dir().parent))
        await interaction.followup.send(
            file=discord.File(io.BytesIO(png), filename=f"profile-{uid}.png"),
            ephemeral=ephemeral)

    @jq.command(name="me", description="Show your season profile card")
    async def jq_me(self, interaction: discord.Interaction) -> None:
        if not self._guarded(interaction):
            await interaction.response.send_message(embed=embeds.guard_embed(), ephemeral=True)
            return
        await self._send_profile(interaction, interaction.user)

    @jq.command(name="profile", description="Show another player's profile card")
    @app_commands.describe(user="Player to look up")
    async def jq_profile(self, interaction: discord.Interaction, user: discord.Member) -> None:
        if not self._guarded(interaction):
            await interaction.response.send_message(embed=embeds.guard_embed(), ephemeral=True)
            return
        await self._send_profile(interaction, user)

    @jq.command(name="leaderboard", description="Season global leaderboard")
    async def jq_leaderboard(self, interaction: discord.Interaction) -> None:
        if not self._guarded(interaction):
            await interaction.response.send_message(embed=embeds.guard_embed(), ephemeral=True)
            return
        rows = await self.db.leaderboard(10)
        embed = discord.Embed(title=f"🏆 Season {self.season.get('id', 1)} leaderboard",
                              colour=discord.Colour(0x5865F2))
        if not rows:
            embed.description = "No scores yet — start a quiz!"
        else:
            medals = ["🥇", "🥈", "🥉"]
            lines = []
            for i, r in enumerate(rows, 1):
                medal = medals[i - 1] if i <= 3 else f"{i}."
                acc = round(100 * r["correct"] / max(1, r["correct"] + r["mistakes"]), 1)
                lines.append(f"{medal} **{r['name']}** — {r['exp']:,} EXP "
                             f"(`{self._rank_name(r['rank_id'])}` • {acc}% acc)")
            embed.description = "\n".join(lines)
        embed.set_footer(text=f"{self.days_left()} days left • mistakes never cost EXP")
        await interaction.response.send_message(embed=embed)

    @jq.command(name="info", description="Ranks, EXP, bonuses and badges explained")
    async def jq_info(self, interaction: discord.Interaction) -> None:
        embed = discord.Embed(title="JLPT Quiz — competitive guide", colour=discord.Colour(0x5865F2))
        base = self.exp_cfg.get("base_by_level", {})
        embed.add_field(
            name="EXP per correct",
            value=" • ".join(f"{k}={v}" for k, v in base.items()) +
                  " — only the scorer gains EXP; mistakes never cost EXP.",
            inline=False)
        lines = []
        for r in self.ranks_cfg:
            gates = " ".join(f"{k}≥{v}" for k, v in (r.get("gates") or {}).items())
            trial = " + trial" if r.get("trials") else ""
            lines.append(f"`{r['en']}` {r.get('threshold', 0):,} {gates}{trial}")
        embed.add_field(name="Ranks (need EXP + level quotas)", value="\n".join(lines), inline=False)
        embed.add_field(
            name="Bonuses",
            value="Speed <5s +25% • streak 3/5/10 +10/+25/+60 • clean win +100 • "
                  "comeback +50 • giant-slay +50 • first answer of day +50 • weekends ×2. "
                  "Daily soft cap: full → half → 10%.",
            inline=False)
        embed.add_field(
            name="Rules",
            value="First press decides each question (correct +1, wrong = mistake +1) "
                  "and advances immediately — no brute-forcing. Clean session = session win "
                  "with zero mistakes. `/jq badge` manages your 8 display badges.",
            inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @jq.command(name="badge", description="Manage your 8 display badges")
    async def jq_badge(self, interaction: discord.Interaction) -> None:
        if not self._guarded(interaction):
            await interaction.response.send_message(embed=embeds.guard_embed(), ephemeral=True)
            return
        uid = interaction.user.id
        await self.db.upsert_player(uid, _display_name(interaction.user))
        owned = await self.db.owned_badges(uid)
        if not owned:
            await interaction.response.send_message(
                "No badges yet — play quizzes to earn them!", ephemeral=True)
            return
        equipped = [o for o in owned if o["equipped"]]
        desc = "Shown on your card:\n" + (
            "\n".join(f"• {self.badge_map[o['badge_id']]['en']}" for o in equipped) or "(none)")
        await interaction.response.send_message(
            content=desc, view=BadgeView(self, uid, owned, self.badge_map), ephemeral=True)

    # ---------- background ----------

    @tasks.loop(seconds=30.0)
    async def idle_watcher(self) -> None:
        await self.ensure_season()
        session = await self.manager.get()
        if session is None:
            return
        if session.idle_seconds() < self.settings.idle_timeout_sec:
            return
        log.info("session %s idle timeout (%.0fs)", session.session_id, session.idle_seconds())
        session.close()
        notes = await self.on_session_end(session, "idle timeout")
        channel = self.bot.get_channel(self.settings.channel_id)
        try:
            if channel is not None and isinstance(channel, discord.abc.Messageable):
                if session.message_id is not None:
                    try:
                        msg = await channel.fetch_message(session.message_id)  # type: ignore[attr-defined]
                        dead = QuizView(session=session, manager=self.manager, settings=self.settings)
                        dead._disable()
                        await msg.edit(view=dead)
                    except Exception:
                        pass
                await channel.send(  # type: ignore[attr-defined]
                    content=notes or None, embed=embeds.timeout_embed(session))
        except Exception:
            log.exception("failed to post timeout message")
        finally:
            await self.manager.stop()

    @idle_watcher.before_loop
    async def _before_idle(self) -> None:
        await self.bot.wait_until_ready()
