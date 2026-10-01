"""Progression math tests: EXP, gates, trials, ranks, soft cap."""

import datetime as dt

from jlpt_bot import progression as p

CFG = {
    "base_by_level": {"N5": 10, "N4": 20, "N3": 40, "N2": 80, "N1": 150},
    "speed_bonus": {"within_sec": 5, "pct": 25},
    "streak_bonus": [{"n": 3, "flat": 10}, {"n": 5, "flat": 25}],
    "daily_soft_cap": [{"upto": 100, "mult": 1.0}, {"mult": 0.1}],
    "weekend_double": True,
}
RANKS = [
    {"id": "houga", "threshold": 0},
    {"id": "reimei", "threshold": 2000, "gates": {"N5": 20}},
    {"id": "saku", "threshold": 8000, "gates": {"N5": 60, "N4": 30}},
    {"id": "ryuusei", "threshold": 260000, "gates": {"N2": 200},
     "trials": [{"type": "accuracy_window", "n": 100, "min_acc": 0.80, "levels": ["N2", "N1"]}]},
]


def test_base_scales_with_level():
    assert p.base_exp_for_level("N5") == 10
    assert p.base_exp_for_level("N1") == 150


def test_speed_and_streak_bonus():
    exp, names = p.answer_exp("N1", 2.0, 1, 0, False, CFG)
    assert exp == int(150 * 1.25) and names == ["speed"]
    exp5, names5 = p.answer_exp("N5", 9.0, 5, 0, False, CFG)
    assert exp5 == 10 + 25 and names5 == ["streak5"]


def test_soft_cap_and_weekend():
    exp, _ = p.answer_exp("N1", 9.0, 1, 150, False, CFG)
    assert exp == max(1, int(150 * 0.1))
    expw, namesw = p.answer_exp("N5", 9.0, 1, 0, True, CFG)
    assert expw == 20 and "weekend" in namesw


def test_gates_block_grinders():
    assert p.rank_index_for(99999, {}, RANKS, [], 0, 0) == 0
    assert p.rank_index_for(3000, {"N5": 25}, RANKS, [], 0, 0) == 1
    assert p.rank_index_for(9000, {"N5": 60, "N4": 30}, RANKS, [], 0, 0) == 2


def test_trial_blocks_without_accuracy():
    per = {"N5": 60, "N4": 30, "N2": 250}
    recent = [{"level": "N2", "correct": i < 70} for i in range(100)]
    assert p.rank_index_for(300000, per, RANKS, recent, 0, 0) == 2
    good = [{"level": "N2", "correct": i < 85} for i in range(100)]
    assert p.rank_index_for(300000, per, RANKS, good, 0, 0) == 3


def test_weekend_helper():
    assert p.is_weekend(dt.datetime(2026, 10, 3)) is True  # Saturday
    assert p.is_weekend(dt.datetime(2026, 10, 5)) is False  # Monday


def test_lifetime_ceiling():
    assert p.lifetime_exp(100, [200, 300], 1_000_000) == 600
    assert p.lifetime_exp(900_000, [500_000], 1_000_000) == 1_000_000
