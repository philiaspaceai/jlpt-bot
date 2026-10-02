"""Store tests: loading, category counts, sampling."""

import random

from jlpt_dojo.categories import CATEGORIES, classify
from jlpt_dojo.store import ALL_LEVELS, QuestionStore


def test_load_real_data():
    store = QuestionStore.load("data")
    assert store.total("N5") == 426
    assert store.total("N4") == 641
    assert store.total("N1") > 1000
    assert store.total(ALL_LEVELS) == sum(store.total(l) for l in ["N5", "N4", "N3", "N2", "N1"])


def test_category_counts_cover_every_question():
    store = QuestionStore.load("data")
    for level in ["N5", "N4", "N3", "N2", "N1"]:
        counts = store.category_counts(level)
        assert sum(counts.values()) == store.total(level)
        assert set(counts) <= {c.id for c in CATEGORIES}


def test_sample_is_random_and_bounded():
    store = QuestionStore.load("data")
    first = [q.id for q in store.sample("N5", "ALL", 5, random.Random(1))]
    second = [q.id for q in store.sample("N5", "ALL", 5, random.Random(2))]
    assert len(first) == 5
    # Different seeds almost always give different samples for this dataset.
    assert first != second
    # Count clamps to pool size.
    huge = store.sample("N5", "ALL", 9999, random.Random(0))
    assert len(huge) == store.total("N5")


def test_sample_category_filter():
    store = QuestionStore.load("data")
    sampled = store.sample("N1", "grammar", 5, random.Random(0))
    assert sampled
    assert all(classify(q.instruction) == "grammar" for q in sampled)
