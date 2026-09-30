"""Session tests: fastest-finger scoring, stale handling, single session."""

import random

import pytest

from jlpt_bot.models import QuizConfig
from jlpt_bot.quiz import QuizManager, QuizSession
from jlpt_bot.store import QuestionStore, shuffle_options


def _config() -> QuizConfig:
    return QuizConfig(
        level="N5",
        type_id="ALL",
        type_label="ALL",
        count=5,
        starter_id=111,
        starter_name="starter",
        guild_id=1,
        channel_id=2,
    )


def _session(n: int = 3) -> QuizSession:
    store = QuestionStore.load("data")
    pool = store.sample("N5", "ALL", n, random.Random(0))
    shuffled = [shuffle_options(q, random.Random(i)) for i, q in enumerate(pool)]
    return QuizSession(config=_config(), questions=shuffled)


@pytest.mark.asyncio
async def test_first_correct_wins_and_auto_advances():
    sess = _session(2)
    correct = sess.current().displayed_answer  # type: ignore[union-attr]
    res = await sess.answer(10, "A", correct, 0)
    assert res.kind == "correct"
    assert sess.scores[10].points == 1
    assert sess.current_index == 1
    # Same old index is now stale.
    res2 = await sess.answer(20, "B", correct, 0)
    assert res2.kind == "stale"


@pytest.mark.asyncio
async def test_wrong_is_ignored_no_score_no_advance():
    sess = _session(1)
    cur = sess.current()
    assert cur is not None
    wrong = 1 if cur.displayed_answer != 1 else 2
    res = await sess.answer(10, "A", wrong, 0)
    assert res.kind == "wrong"
    assert 10 not in sess.scores
    assert sess.current_index == 0


@pytest.mark.asyncio
async def test_finish_and_leaderboard_order():
    sess = _session(2)
    for idx in range(2):
        cur = sess.current()
        assert cur is not None
        await sess.answer(10 if idx == 0 else 20, f"P{idx}", cur.displayed_answer, idx)
    assert sess.is_finished()
    board = sess.leaderboard()
    assert len(board) == 2
    # Same points -> alphabetical.
    assert [s.points for s in board] == [1, 1]


@pytest.mark.asyncio
async def test_manager_single_session():
    mgr = QuizManager()
    s1 = await mgr.start(_config(), _session(1).questions)
    assert s1 is not None
    s2 = await mgr.start(_config(), _session(1).questions)
    assert s2 is None  # rejected while active
    await mgr.stop()
    s3 = await mgr.start(_config(), _session(1).questions)
    assert s3 is not None
    await mgr.stop()


def test_stop_permission():
    sess = _session(1)
    assert sess.can_stop(111, False) is True  # starter
    assert sess.can_stop(999, False) is False
    assert sess.can_stop(999, True) is True  # admin
