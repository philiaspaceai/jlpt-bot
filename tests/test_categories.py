"""Category tests: every bundled instruction maps to exactly one broad bucket."""

import json

from jlpt_bot.categories import CATEGORIES, classify
from jlpt_bot.store import LEVELS, QuestionStore

# Snapshot of the mapping analysis (2026-09-30). If data grows, update the
# table deliberately — a count shift means a rule regressed or new wording.
EXPECTED_COUNTS = {
    "N5": {"vocab": 45, "grammar": 69, "reading": 12},
    "N4": {"vocab": 115, "grammar": 178, "reading": 48},
    "N3": {"vocab": 359, "grammar": 501, "reading": 240},
    "N2": {"vocab": 320, "grammar": 499, "reading": 279},
    "N1": {"vocab": 288, "grammar": 419, "reading": 376},
}

VALID_IDS = {c.id for c in CATEGORIES} | {"reading"}  # reading is the safety net


def test_every_instruction_classifies():
    store = QuestionStore.load("data")
    for level in LEVELS:
        for q in store._pool(level, "ALL"):
            assert classify(q.instruction) in {c.id for c in CATEGORIES}


def test_snapshot_counts_per_level():
    store = QuestionStore.load("data")
    for level, expected in EXPECTED_COUNTS.items():
        assert store.category_counts(level) == expected


def test_representative_instructions():
    assert classify("もんだい1 ____ の ことばは ひらがなで どう かきますか。") == "vocab"
    assert classify("問題2 ______のことばを漢字で書くとき、最もよいものを選べ") == "vocab"
    assert classify("問題3 ______の言葉に意味が最も近いものを選べ") == "vocab"
    assert classify("問題5 つぎのことばの使い方として最もよいものを選べ") == "vocab"
    assert classify("もんだい1 ( )に何を入れますか。") == "grammar"
    assert classify("問題2 次の文の★に入る最もよいものを選べ") == "grammar"
    assert classify("問題3 つぎの文章を読んで、19から23の中に入るものを選べ") == "grammar"
    assert classify("問題6 つぎの文章を読んで、質問に答えなさい。") == "reading"
    assert classify("問題12 次のAとBの文章を読んで、答えを選べ") == "reading"


def test_raw_json_never_edited():
    """Guard: data files keep their original schema (no category column)."""
    for level in LEVELS:
        raw = json.load(open(f"data/{level}.json"))
        assert raw, level
        for item in raw:
            assert set(item) == {
                "id",
                "instruction",
                "passage",
                "stem",
                "target",
                "options",
                "answer",
                "correctOrder",
            }, level
