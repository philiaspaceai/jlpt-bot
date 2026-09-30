"""Embed smoke tests: discord.Embed builders never crash and stay in limits."""

import random

from jlpt_bot import embeds
from jlpt_bot.models import QuizConfig
from jlpt_bot.quiz import QuizSession
from jlpt_bot.store import QuestionStore, shuffle_options


def _sess() -> QuizSession:
    store = QuestionStore.load("data")
    pool = store.sample("N5", "ALL", 5, random.Random(0))
    shuffled = [shuffle_options(q, random.Random(i)) for i, q in enumerate(pool)]
    cfg = QuizConfig("N5", "ALL", "ALL", 5, 1, "starter", 1, 2)
    return QuizSession(config=cfg, questions=shuffled)


def test_embeds_within_discord_limits():
    s = _sess()
    for e in [
        embeds.setup_embed(),
        embeds.question_embed(s),
        embeds.finished_embed(s),
        embeds.timeout_embed(s),
        embeds.stopped_embed(s, "starter"),
        embeds.busy_embed(),
    ]:
        assert e.title
        assert len(e.title or "") <= 256
        if e.description:
            assert len(e.description) <= 4096
        for f in e.fields:
            assert len(f.name) <= 256
            assert len(f.value) <= 1024
