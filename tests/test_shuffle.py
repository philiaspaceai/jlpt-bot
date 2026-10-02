"""Shuffle tests: anti pattern-recognition keeps the answer correct."""

import random

from jlpt_dojo.models import Question
from jlpt_dojo.store import shuffle_options


def _q() -> Question:
    return Question(
        id=0,
        level="N5",
        instruction="mondai1",
        passage=None,
        stem="stem",
        target=None,
        options=["a", "b", "c", "d"],
        answer=2,  # b
        correct_order=None,
    )


def test_shuffle_keeps_correct_option():
    for seed in range(50):
        s = shuffle_options(_q(), random.Random(seed))
        assert sorted(s.displayed_options) == ["a", "b", "c", "d"]
        assert s.displayed_options[s.displayed_answer - 1] == "b"


def test_shuffle_varies_positions():
    seen = set()
    for seed in range(30):
        s = shuffle_options(_q(), random.Random(seed))
        seen.add(s.displayed_answer)
    # With 30 seeds we must observe more than one position.
    assert len(seen) > 1
