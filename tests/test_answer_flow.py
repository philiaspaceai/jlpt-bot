"""Answer pipeline tests: strip buttons, reveal message, next as new message."""

import random
from types import SimpleNamespace
from unittest.mock import AsyncMock

import discord
import pytest

from jlpt_dojo import embeds
from jlpt_dojo.config import Settings
from jlpt_dojo.models import QuizConfig
from jlpt_dojo.quiz import QuizManager, QuizSession
from jlpt_dojo.store import QuestionStore, shuffle_options
from jlpt_dojo.views import QuizView


def _session(n: int = 2) -> QuizSession:
    store = QuestionStore.load("data")
    pool = store.sample("N5", "ALL", n, random.Random(0))
    shuffled = [shuffle_options(q, random.Random(i)) for i, q in enumerate(pool)]
    cfg = QuizConfig("N5", "ALL", "ALL", n, 1, "starter", 1, 2)
    return QuizSession(config=cfg, questions=shuffled)


def _interaction(view, correct: bool):
    user = SimpleNamespace(id=10, display_name="A")
    channel = AsyncMock(spec=discord.abc.Messageable)
    channel.send.return_value = SimpleNamespace(id=777)
    return SimpleNamespace(
        guild_id=1, channel_id=2, user=user,
        response=AsyncMock(), channel=channel,
        followup=AsyncMock(), client=SimpleNamespace(),
    ), channel


def test_reveal_embed_contents():
    e = embeds.reveal_embed(1, 5, 2, "b", True, "A", 2, "b")
    assert "✅" in (e.title or "") and "1/5" in (e.title or "")
    w = embeds.reveal_embed(2, 5, 1, "a", False, "B", 2, "b", 3)
    assert "❌" in (w.title or "") and "mistake #3" in (w.title or "")


@pytest.mark.asyncio
async def test_correct_press_posts_reveal_then_next():
    mgr = QuizManager()
    sess = _session(2)
    settings = Settings(token="x", guild_id=1, channel_id=2)
    view = QuizView(session=sess, manager=mgr, settings=settings)
    interaction, channel = _interaction(view, True)
    btn = next(c for c in view.children if getattr(c, "label", None) == "1")
    # Force pick the correct displayed answer.
    correct = sess.current().displayed_answer  # type: ignore[union-attr]
    target = next(c for c in view.children if getattr(c, "label", None) == str(correct))
    await target.callback(interaction)
    # Buttons stripped on the question message...
    interaction.response.edit_message.assert_awaited_once()
    # ...then reveal + next question as new messages.
    assert channel.send.await_count == 2
    first_embed = channel.send.call_args_list[0].kwargs["embed"]
    assert "✅" in (first_embed.title or "")
    assert sess.message_id == 777


@pytest.mark.asyncio
async def test_wrong_press_posts_reveal_and_advances():
    sess = _session(1)
    settings = Settings(token="x", guild_id=1, channel_id=2)
    view = QuizView(session=sess, manager=QuizManager(), settings=settings)
    interaction, channel = _interaction(view, False)
    cur = sess.current()
    assert cur is not None
    wrong = 1 if cur.displayed_answer != 1 else 2
    btn = next(c for c in view.children if getattr(c, "label", None) == str(wrong))
    await btn.callback(interaction)
    assert channel.send.await_count == 2  # reveal + final leaderboard
    first_embed = channel.send.call_args_list[0].kwargs["embed"]
    assert "❌" in (first_embed.title or "")
    assert sess.is_finished()
