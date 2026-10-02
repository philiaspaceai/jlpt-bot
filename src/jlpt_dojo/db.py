"""SQLite season store. One writer lock, WAL mode, whole-file season archive.

A season rollover closes this file, renames it into archive_dir, and starts
a fresh file at the same path. Lifetime numbers are summed across archives.
"""

from __future__ import annotations

import asyncio
import datetime as dt
import json
import sqlite3
import time
from pathlib import Path

import aiosqlite

SCHEMA = """
PRAGMA journal_mode=WAL;
CREATE TABLE IF NOT EXISTS kv (k TEXT PRIMARY KEY, v TEXT);
CREATE TABLE IF NOT EXISTS seasons (
  id INTEGER PRIMARY KEY, started_ts REAL NOT NULL, ends_ts REAL NOT NULL);
CREATE TABLE IF NOT EXISTS players (
  user_id INTEGER PRIMARY KEY, name TEXT NOT NULL, rank_id TEXT NOT NULL DEFAULT 'houga',
  updated_ts REAL NOT NULL);
CREATE TABLE IF NOT EXISTS season_stats (
  user_id INTEGER PRIMARY KEY, season_id INTEGER NOT NULL DEFAULT 1,
  exp INTEGER NOT NULL DEFAULT 0, answers INTEGER NOT NULL DEFAULT 0,
  correct INTEGER NOT NULL DEFAULT 0, mistakes INTEGER NOT NULL DEFAULT 0,
  cur_streak INTEGER NOT NULL DEFAULT 0, best_streak INTEGER NOT NULL DEFAULT 0,
  best_n1_streak INTEGER NOT NULL DEFAULT 0, cur_n1_streak INTEGER NOT NULL DEFAULT 0,
  wins INTEGER NOT NULL DEFAULT 0, first_bloods INTEGER NOT NULL DEFAULT 0,
  clean_sessions INTEGER NOT NULL DEFAULT 0, comebacks INTEGER NOT NULL DEFAULT 0,
  giant_slays INTEGER NOT NULL DEFAULT 0,
  resp_ms_total INTEGER NOT NULL DEFAULT 0, resp_count INTEGER NOT NULL DEFAULT 0,
  fastest_ms INTEGER, day_streak INTEGER NOT NULL DEFAULT 0,
  last_day TEXT, correct_today INTEGER NOT NULL DEFAULT 0, today_day TEXT,
  per_level TEXT NOT NULL DEFAULT '{}');
CREATE TABLE IF NOT EXISTS answers_log (
  id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL,
  season_id INTEGER NOT NULL, ts REAL NOT NULL, level TEXT NOT NULL,
  correct INTEGER NOT NULL, ms INTEGER, session_tag TEXT);
CREATE INDEX IF NOT EXISTS idx_answers_user ON answers_log(user_id, id);
CREATE TABLE IF NOT EXISTS sessions (
  id TEXT PRIMARY KEY, season_id INTEGER NOT NULL, started_ts REAL NOT NULL,
  ended_ts REAL, winner_id INTEGER, half_leader_id INTEGER, q_total INTEGER NOT NULL DEFAULT 0);
CREATE TABLE IF NOT EXISTS badges (
  user_id INTEGER NOT NULL, badge_id TEXT NOT NULL, equipped INTEGER NOT NULL DEFAULT 0,
  slot INTEGER NOT NULL DEFAULT 0, awarded_ts REAL NOT NULL,
  PRIMARY KEY (user_id, badge_id));
"""


def season_exp_from_file(path: str | Path) -> dict[int, int]:
    """Read {user_id: exp} from an archived (or live) db file. Read-only."""
    try:
        con = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
        rows = con.execute("SELECT user_id, exp FROM season_stats").fetchall()
        con.close()
        return {int(u): int(e) for u, e in rows}
    except Exception:
        return {}


class Database:
    def __init__(self, path: str | Path, archive_dir: str | Path) -> None:
        self.path = Path(path)
        self.archive_dir = Path(archive_dir)
        self._lock = asyncio.Lock()
        self._db: aiosqlite.Connection | None = None

    async def open(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.archive_dir.mkdir(parents=True, exist_ok=True)
        self._db = await aiosqlite.connect(self.path)
        await self._db.executescript(SCHEMA)
        await self._db.commit()

    async def close(self) -> None:
        if self._db is not None:
            await self._db.close()
            self._db = None

    async def ensure_season(self, months: int, now: float | None = None) -> dict:
        """Return current season row, rolling over (archive + fresh) if expired."""
        now = now if now is not None else time.time()
        async with self._lock:
            assert self._db is not None
            cur = await self._db.execute("SELECT id, started_ts, ends_ts FROM seasons ORDER BY id DESC LIMIT 1")
            row = await cur.fetchone()
            if row is not None and now < float(row[2]):
                return {"id": int(row[0]), "started_ts": float(row[1]), "ends_ts": float(row[2])}
            new_id = (int(row[0]) + 1) if row is not None else 1
            if row is not None:
                await self._db.close()
                target = self.archive_dir / f"quiz-season-{int(row[0])}.db"
                self.path.rename(target)
                self._db = await aiosqlite.connect(self.path)
                await self._db.executescript(SCHEMA)
            ends = now + months * 30 * 24 * 3600
            await self._db.execute(
                "INSERT INTO seasons (id, started_ts, ends_ts) VALUES (?, ?, ?)", (new_id, now, ends))
            await self._db.commit()
            return {"id": new_id, "started_ts": now, "ends_ts": ends}

    async def upsert_player(self, user_id: int, name: str) -> None:
        async with self._lock:
            assert self._db is not None
            await self._db.execute(
                "INSERT INTO players (user_id, name, rank_id, updated_ts) VALUES (?, ?, 'houga', ?) "
                "ON CONFLICT(user_id) DO UPDATE SET name=excluded.name, updated_ts=excluded.updated_ts",
                (user_id, name, time.time()))
            await self._db.execute(
                "INSERT OR IGNORE INTO season_stats (user_id) VALUES (?)", (user_id,))
            await self._db.commit()

    async def get_stats(self, user_id: int) -> dict:
        async with self._lock:
            assert self._db is not None
            await self._db.execute("INSERT OR IGNORE INTO season_stats (user_id) VALUES (?)", (user_id,))
            cur = await self._db.execute("SELECT * FROM season_stats WHERE user_id=?", (user_id,))
            row = await cur.fetchone()
            cols = [d[0] for d in cur.description]
            data = dict(zip(cols, row))
            data["per_level"] = json.loads(data.get("per_level") or "{}")
            cur2 = await self._db.execute("SELECT rank_id FROM players WHERE user_id=?", (user_id,))
            r = await cur2.fetchone()
            data["rank_id"] = r[0] if r else "houga"
            return data

    async def add_exp(self, user_id: int, exp: int) -> int:
        async with self._lock:
            assert self._db is not None
            await self._db.execute("INSERT OR IGNORE INTO season_stats (user_id) VALUES (?)", (user_id,))
            await self._db.execute("UPDATE season_stats SET exp = exp + ? WHERE user_id=?", (exp, user_id))
            await self._db.commit()
            cur = await self._db.execute("SELECT exp FROM season_stats WHERE user_id=?", (user_id,))
            return int((await cur.fetchone())[0])

    async def record_answer(
        self, user_id: int, season_id: int, level: str, correct: bool,
        ms: int | None, session_tag: str, day: str, hour: int,
    ) -> dict:
        """Update aggregates + log. Returns fresh stats dict (caller holds no lock)."""
        async with self._lock:
            assert self._db is not None
            await self._db.execute("INSERT OR IGNORE INTO season_stats (user_id) VALUES (?)", (user_id,))
            cur = await self._db.execute("SELECT * FROM season_stats WHERE user_id=?", (user_id,))
            row = await cur.fetchone()
            cols = [d[0] for d in cur.description]
            s = dict(zip(cols, row))
            per = json.loads(s.get("per_level") or "{}")
            lvl = per.get(level, {"c": 0, "m": 0})
            s["answers"] = int(s["answers"]) + 1
            if correct:
                s["correct"] = int(s["correct"]) + 1
                s["cur_streak"] = int(s["cur_streak"]) + 1
                s["best_streak"] = max(int(s["best_streak"]), int(s["cur_streak"]))
                lvl["c"] = lvl.get("c", 0) + 1
                if level == "N1":
                    s["cur_n1_streak"] = int(s["cur_n1_streak"]) + 1
                    s["best_n1_streak"] = max(int(s["best_n1_streak"]), int(s["cur_n1_streak"]))
                if ms is not None:
                    s["resp_ms_total"] = int(s["resp_ms_total"]) + ms
                    s["resp_count"] = int(s["resp_count"]) + 1
                    if s["fastest_ms"] is None or ms < int(s["fastest_ms"]):
                        s["fastest_ms"] = ms
                if s.get("today_day") != day:
                    s["today_day"] = day
                    s["correct_today"] = 1
                    s["day_streak"] = int(s["day_streak"]) + 1 if s.get("last_day") else 1
                    s["last_day"] = day
                    first_today = True
                else:
                    s["correct_today"] = int(s["correct_today"]) + 1
                    first_today = False
            else:
                s["mistakes"] = int(s["mistakes"]) + 1
                s["cur_streak"] = 0
                s["cur_n1_streak"] = 0
                lvl["m"] = lvl.get("m", 0) + 1
                first_today = False
            per[level] = lvl
            s["per_level"] = json.dumps(per)
            sets = ("answers=?, correct=?, mistakes=?, cur_streak=?, best_streak=?, "
                    "cur_n1_streak=?, best_n1_streak=?, resp_ms_total=?, resp_count=?, fastest_ms=?, "
                    "day_streak=?, last_day=?, today_day=?, correct_today=?, per_level=?")
            await self._db.execute(
                f"UPDATE season_stats SET {sets} WHERE user_id=?",
                (s["answers"], s["correct"], s["mistakes"], s["cur_streak"], s["best_streak"],
                 s["cur_n1_streak"], s["best_n1_streak"], s["resp_ms_total"], s["resp_count"],
                 s["fastest_ms"], s["day_streak"], s["last_day"], s["today_day"],
                 s["correct_today"], s["per_level"], user_id))
            await self._db.execute(
                "INSERT INTO answers_log (user_id, season_id, ts, level, correct, ms, session_tag) "
                "VALUES (?, ?, ?, ?, ?, ?, ?)",
                (user_id, season_id, time.time(), level, 1 if correct else 0, ms, session_tag))
            await self._db.commit()
            s["first_today"] = first_today
            s["per_level"] = per
            return s

    async def recent_answers(self, user_id: int, n: int) -> list[dict]:
        async with self._lock:
            assert self._db is not None
            cur = await self._db.execute(
                "SELECT level, correct FROM answers_log WHERE user_id=? ORDER BY id DESC LIMIT ?",
                (user_id, n))
            rows = await cur.fetchall()
            return [{"level": lvl, "correct": bool(c)} for lvl, c in reversed(rows)]

    async def correct_today_count(self, user_id: int, day: str) -> int:
        async with self._lock:
            assert self._db is not None
            cur = await self._db.execute(
                "SELECT COUNT(*) FROM answers_log WHERE user_id=? AND correct=1 "
                "AND datetime(ts, 'unixepoch') >= date(?)",
                (user_id, day))
            row = await cur.fetchone()
            return int(row[0]) if row else 0

    async def mark_first_blood(self, user_id: int) -> None:
        async with self._lock:
            assert self._db is not None
            await self._db.execute("UPDATE season_stats SET first_bloods = first_bloods + 1 WHERE user_id=?", (user_id,))
            await self._db.commit()

    async def record_session_end(
        self, session_tag: str, season_id: int, winner_id: int | None,
        half_leader_id: int | None, q_total: int,
    ) -> None:
        async with self._lock:
            assert self._db is not None
            await self._db.execute(
                "INSERT OR REPLACE INTO sessions (id, season_id, started_ts, ended_ts, winner_id, half_leader_id, q_total) "
                "VALUES (?, ?, ?, ?, ?, ?, ?)",
                (session_tag, season_id, time.time(), time.time(), winner_id, half_leader_id, q_total))
            if winner_id is not None:
                await self._db.execute("UPDATE season_stats SET wins = wins + 1 WHERE user_id=?", (winner_id,))
                if half_leader_id is not None and half_leader_id != winner_id:
                    await self._db.execute(
                        "UPDATE season_stats SET comebacks = comebacks + 1 WHERE user_id=?", (winner_id,))
            await self._db.commit()

    async def record_clean_session(self, user_id: int) -> None:
        async with self._lock:
            assert self._db is not None
            await self._db.execute(
                "UPDATE season_stats SET clean_sessions = clean_sessions + 1 WHERE user_id=?", (user_id,))
            await self._db.commit()

    async def record_giant_slay(self, user_id: int) -> None:
        async with self._lock:
            assert self._db is not None
            await self._db.execute(
                "UPDATE season_stats SET giant_slays = giant_slays + 1 WHERE user_id=?", (user_id,))
            await self._db.commit()

    async def set_rank(self, user_id: int, rank_id: str) -> None:
        async with self._lock:
            assert self._db is not None
            await self._db.execute("UPDATE players SET rank_id=? WHERE user_id=?", (rank_id, user_id))
            await self._db.commit()

    async def award_badge(self, user_id: int, badge_id: str, auto_equip: bool = True) -> bool:
        """Returns True if newly awarded."""
        async with self._lock:
            assert self._db is not None
            cur = await self._db.execute(
                "SELECT 1 FROM badges WHERE user_id=? AND badge_id=?", (user_id, badge_id))
            if await cur.fetchone():
                return False
            slot = 0
            if auto_equip:
                cur2 = await self._db.execute(
                    "SELECT COUNT(*) FROM badges WHERE user_id=? AND equipped=1", (user_id,))
                if int((await cur2.fetchone())[0]) < 8:
                    cur3 = await self._db.execute(
                        "SELECT COALESCE(MAX(slot), -1) FROM badges WHERE user_id=? AND equipped=1", (user_id,))
                    slot = int((await cur3.fetchone())[0]) + 1
                    await self._db.execute(
                        "INSERT INTO badges (user_id, badge_id, equipped, slot, awarded_ts) VALUES (?, ?, 1, ?, ?)",
                        (user_id, badge_id, slot, time.time()))
                    await self._db.commit()
                    return True
            await self._db.execute(
                "INSERT INTO badges (user_id, badge_id, equipped, slot, awarded_ts) VALUES (?, ?, 0, 0, ?)",
                (user_id, badge_id, time.time()))
            await self._db.commit()
            return True

    async def set_equipped(self, user_id: int, badge_id: str, equipped: bool) -> bool:
        async with self._lock:
            assert self._db is not None
            if equipped:
                cur = await self._db.execute(
                    "SELECT COUNT(*) FROM badges WHERE user_id=? AND equipped=1", (user_id,))
                if int((await cur.fetchone())[0]) >= 8:
                    return False
                cur2 = await self._db.execute(
                    "SELECT COALESCE(MAX(slot), -1) FROM badges WHERE user_id=? AND equipped=1", (user_id,))
                slot = int((await cur2.fetchone())[0]) + 1
                await self._db.execute(
                    "UPDATE badges SET equipped=1, slot=? WHERE user_id=? AND badge_id=?", (slot, user_id, badge_id))
            else:
                await self._db.execute(
                    "UPDATE badges SET equipped=0, slot=0 WHERE user_id=? AND badge_id=?", (user_id, badge_id))
            await self._db.commit()
            return True

    async def equipped_badges(self, user_id: int) -> list[dict]:
        async with self._lock:
            assert self._db is not None
            cur = await self._db.execute(
                "SELECT badge_id, slot FROM badges WHERE user_id=? AND equipped=1 ORDER BY slot", (user_id,))
            return [{"badge_id": b, "slot": s} for b, s in await cur.fetchall()]

    async def owned_badges(self, user_id: int) -> list[dict]:
        async with self._lock:
            assert self._db is not None
            cur = await self._db.execute(
                "SELECT badge_id, equipped, slot FROM badges WHERE user_id=? ORDER BY awarded_ts", (user_id,))
            return [{"badge_id": b, "equipped": bool(e), "slot": s} for b, e, s in await cur.fetchall()]

    async def leaderboard(self, limit: int = 10) -> list[dict]:
        async with self._lock:
            assert self._db is not None
            cur = await self._db.execute(
                "SELECT s.user_id, COALESCE(p.name, '?'), s.exp, s.correct, s.mistakes, p.rank_id "
                "FROM season_stats s LEFT JOIN players p ON p.user_id = s.user_id "
                "ORDER BY s.exp DESC LIMIT ?", (limit,))
            return [
                {"user_id": u, "name": n, "exp": e, "correct": c, "mistakes": m, "rank_id": r}
                for u, n, e, c, m, r in await cur.fetchall()
            ]

    async def start_session_row(self, session_tag: str, season_id: int, q_total: int) -> None:
        async with self._lock:
            assert self._db is not None
            await self._db.execute(
                "INSERT OR REPLACE INTO sessions (id, season_id, started_ts, q_total) VALUES (?, ?, ?, ?)",
                (session_tag, season_id, time.time(), q_total))
            await self._db.commit()

    async def user_had_session_today(self, user_id: int, day_start_ts: float) -> bool:
        async with self._lock:
            assert self._db is not None
            cur = await self._db.execute(
                "SELECT 1 FROM answers_log WHERE user_id=? AND ts >= ? LIMIT 1", (user_id, day_start_ts))
            return (await cur.fetchone()) is not None

    async def sessions_played(self, user_id: int) -> int:
        async with self._lock:
            assert self._db is not None
            cur = await self._db.execute(
                "SELECT COUNT(DISTINCT session_tag) FROM answers_log WHERE user_id=?", (user_id,))
            row = await cur.fetchone()
            return int(row[0]) if row else 0

    @staticmethod
    def today_day(now: dt.datetime | None = None) -> str:
        return (now or dt.datetime.now()).strftime("%Y-%m-%d")
