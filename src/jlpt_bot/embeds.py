"""All Discord Embed builders in one place.

discord.py 2.7.1 (see docs/discord-py/api.md - discord.Embed).
Keeping every embed here isolates UI-text changes to a single module.
"""

from __future__ import annotations

import discord

from .models import PlayerScore, QuizConfig, ShuffledQuestion
from .quiz import QuizSession

BRAND = 0x5865F2  # blurple
SUCCESS = 0x57F287
WARN = 0xFEE75C
CLOSED = 0xED4245

MAX_FIELD = 1024


def _clip(text: str, limit: int = MAX_FIELD) -> str:
    text = text.strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1] + "…"


def setup_embed() -> discord.Embed:
    embed = discord.Embed(
        title="JLPT Quiz — Setup",
        description=(
            "Pick a level, a question type (mondai group), and a question count.\n"
            "Questions are random every session and options are shuffled."
        ),
        colour=discord.Colour(BRAND),
    )
    embed.add_field(name="Levels", value="N5 / N4 / N3 / N2 / N1 / ALL", inline=True)
    embed.add_field(name="Counts", value="5 / 10 / 15 / 20", inline=True)
    embed.add_field(
        name="Rules",
        value="Fastest correct answer gets +1 and we auto-advance. Wrong answers are ignored.",
        inline=False,
    )
    embed.set_footer(text="Only the quiz starter or a server admin can Stop.")
    return embed


def _question_body(q: ShuffledQuestion) -> str:
    lines: list[str] = []
    lines.append(f"**{q.source.instruction}**")
    if q.source.passage:
        lines.append(_clip(q.source.passage, 900))
    stem = q.source.stem
    if q.source.target:
        # Highlight the target word without changing the stored data.
        stem = stem.replace(q.source.target, f"__**{q.source.target}**__", 1)
    lines.append(f"\n{stem}\n")
    for i, opt in enumerate(q.displayed_options, start=1):
        lines.append(f"**{i}.** {opt}")
    return "\n".join(lines)


def question_embed(session: QuizSession) -> discord.Embed:
    q = session.current()
    assert q is not None
    idx = session.current_index + 1
    total = session.total
    embed = discord.Embed(
        title=f"Q {idx}/{total} — {q.source.level} quiz",
        description=_clip(_question_body(q), 4000),
        colour=discord.Colour(BRAND),
    )
    if session.last_correct_name and session.current_index > 0:
        embed.add_field(
            name="Last point",
            value=f"✅ {session.last_correct_name} (+1)",
            inline=False,
        )
    preview = "No points yet."
    board = session.leaderboard()
    if board:
        preview = " • ".join(f"{s.display_name}: {s.points}" for s in board[:5])
    embed.add_field(name="Live scores", value=_clip(preview, MAX_FIELD), inline=False)
    embed.set_footer(
        text=f"Session {session.session_id} • starter: {session.config.starter_name} • fastest correct +1"
    )
    return embed


def reveal_embed(qnum: int, total: int, picked: int, picked_text: str, correct: bool,
                 picker_name: str, correct_index: int, correct_text: str,
                 mistake_no: int = 0) -> discord.Embed:
    if correct:
        embed = discord.Embed(
            title=f"Q{qnum}/{total} — ✅ {picker_name} (+1)",
            description=f"Correct answer: **{correct_index}. {correct_text}**",
            colour=discord.Colour(SUCCESS),
        )
    else:
        embed = discord.Embed(
            title=f"Q{qnum}/{total} — ❌ {picker_name} (mistake #{mistake_no})",
            description=f"{picker_name} pressed **{picked}. {picked_text}**.\n"
                        f"Correct answer: **{correct_index}. {correct_text}**",
            colour=discord.Colour(CLOSED),
        )
    return embed


def finished_embed(session: QuizSession, reason: str = "Quiz finished!") -> discord.Embed:
    embed = discord.Embed(title=f"🏁 {reason}", colour=discord.Colour(SUCCESS))
    board = session.leaderboard()
    if not board:
        embed.description = "No correct answers this session. Try again!"
        return embed
    lines = []
    medals = ["🥇", "🥈", "🥉"]
    for rank, entry in enumerate(board, start=1):
        medal = medals[rank - 1] if rank <= 3 else f"{rank}."
        lines.append(f"{medal} **{entry.display_name}** — {entry.points} pts")
    embed.description = "\n".join(lines)
    embed.set_footer(text=f"Session {session.session_id} • {session.total} questions")
    return embed


def timeout_embed(session: QuizSession) -> discord.Embed:
    embed = finished_embed(session, reason="Session closed (idle 5 minutes).")
    embed.colour = discord.Colour(WARN)
    return embed


def stopped_embed(session: QuizSession, stopped_by: str) -> discord.Embed:
    embed = finished_embed(session, reason=f"Session stopped by {stopped_by}.")
    embed.colour = discord.Colour(CLOSED)
    return embed


def busy_embed() -> discord.Embed:
    return discord.Embed(
        title="A quiz is already running",
        description="Please wait until the current session finishes or is stopped.",
        colour=discord.Colour(WARN),
    )


def wrong_pool_embed() -> discord.Embed:
    return discord.Embed(
        title="No questions found",
        description="Try another level/type combination.",
        colour=discord.Colour(WARN),
    )


def guard_embed() -> discord.Embed:
    return discord.Embed(
        title="Wrong channel",
        description="This bot only runs in its configured server and channel.",
        colour=discord.Colour(CLOSED),
    )
