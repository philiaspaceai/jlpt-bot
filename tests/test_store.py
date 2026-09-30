"""Store tests: loading, mondai grouping, sampling."""

import random

from jlpt_bot.store import ALL_LEVELS, QuestionStore


def test_load_real_data():
    store = QuestionStore.load("data")
    assert store.total("N5") == 126
    assert store.total("N1") > 1000
    assert store.total(ALL_LEVELS) == sum(store.total(l) for l in ["N5", "N4", "N3", "N2", "N1"])


def test_type_groups_are_mondai_buckets():
    store = QuestionStore.load("data")
    groups = store.type_groups("N5")
    assert len(groups) > 3
    # Every question belongs to exactly one group.
    total = sum(g.total for g in groups)
    assert total == store.total("N5")
    # Type ids are short and unique.
    ids = [g.type_id for g in groups]
    assert len(ids) == len(set(ids))
    assert all(len(g.short_label) <= 100 for g in groups)


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


def test_sample_type_filter():
    store = QuestionStore.load("data")
    groups = store.type_groups("N5")
    gid = groups[0].type_id
    sampled = store.sample("N5", gid, 5, random.Random(0))
    assert sampled
    assert all(q.instruction == groups[0].instruction for q in sampled)
