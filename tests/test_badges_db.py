"""Badge engine + database roundtrip tests (SQLite temp files)."""

import pytest
import yaml

from jlpt_dojo import badges as engine
from jlpt_dojo.db import Database, season_exp_from_file


@pytest.fixture()
def cfg():
    with open("config.yaml", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def test_config_loads_with_10_badges_and_ranks(cfg):
    assert len(cfg["badges"]) == 10
    assert len(cfg["ranks"]) == 10
    assert cfg["ranks"][-1]["threshold"] == 700000


def test_badge_conditions():
    badges = [
        {"id": "b1", "cond": {"type": "best_streak", "n": 5}},
        {"id": "b2", "cond": {"type": "mistakes_total", "n": 100}},
        {"id": "b3", "cond": {"type": "accuracy_window", "n": 20, "min_acc": 0.9}},
        {"id": "b4", "cond": {"type": "night_owl"}},
    ]
    snap = {"best_streak": 7, "mistakes": 3, "first_bloods": 0,
            "clean_sessions": 0, "wins": 0, "giant_slays": 0}
    recent = [{"level": "N3", "correct": True}] * 20
    assert engine.check_badges(badges, snap, recent, {"hour": 2}) == ["b1", "b3", "b4"]
    assert engine.check_badges(badges, snap, recent, {"hour": 12}) == ["b1", "b3"]


@pytest.mark.asyncio
async def test_db_answer_stats_and_badges(tmp_path):
    db = Database(tmp_path / "q.db", tmp_path / "arc")
    await db.open()
    season = await db.ensure_season(2)
    assert season["id"] == 1
    await db.upsert_player(7, "T")
    s = await db.record_answer(7, 1, "N3", True, 3000, "s1", "2026-10-01", 10)
    assert s["correct"] == 1 and s["cur_streak"] == 1 and s["first_today"] is True
    s = await db.record_answer(7, 1, "N3", False, None, "s1", "2026-10-01", 10)
    assert s["mistakes"] == 1 and s["cur_streak"] == 0
    assert await db.add_exp(7, 55) == 55
    assert await db.award_badge(7, "firstblood") is True
    assert await db.award_badge(7, "firstblood") is False  # no double award
    assert await db.set_equipped(7, "firstblood", True) is True
    assert [b["badge_id"] for b in await db.equipped_badges(7)] == ["firstblood"]
    await db.mark_first_blood(7)
    got = await db.get_stats(7)
    assert got["first_bloods"] == 1 and got["rank_id"] == "houga"
    await db.record_session_end("s1", 1, 7, None, 5)
    got2 = await db.get_stats(7)
    assert got2["wins"] == 1
    assert await db.sessions_played(7) == 1
    lb = await db.leaderboard(10)
    assert lb[0]["user_id"] == 7 and lb[0]["exp"] == 55
    await db.close()


@pytest.mark.asyncio
async def test_db_season_rollover_archives_file(tmp_path):
    db = Database(tmp_path / "q.db", tmp_path / "arc")
    await db.open()
    s1 = await db.ensure_season(2)
    await db.upsert_player(9, "U")
    await db.add_exp(9, 77)
    # Force expiry by rolling with a past check: new season only when expired,
    # so simulate expiry via direct row update.
    async with db._lock:
        assert db._db is not None
        await db._db.execute("UPDATE seasons SET ends_ts=0 WHERE id=?", (s1["id"],))
        await db._db.commit()
    s2 = await db.ensure_season(2)
    assert s2["id"] == s1["id"] + 1
    assert (tmp_path / "arc" / f"quiz-season-{s1['id']}.db").exists()
    exp = season_exp_from_file(tmp_path / "arc" / f"quiz-season-{s1['id']}.db")
    assert exp.get(9) == 77
    await db.close()
