"""EXP, rank, trial and bonus math. Pure Python, no discord/db imports.

All numbers come from config.yaml. Functions take plain values so they are
trivially unit-testable.
"""

from __future__ import annotations

import datetime as dt

BASE_EXP = {"N5": 10, "N4": 20, "N3": 40, "N2": 80, "N1": 150}

RANK_ORDER = [
    "houga", "reimei", "saku", "seikou", "meijin",
    "shinsei", "seikan", "ryuusei", "suisei", "shindan",
]


def base_exp_for_level(level: str, table: dict[str, int] | None = None) -> int:
    table = table or BASE_EXP
    return int(table.get(level, 10))


def soft_cap_mult(correct_today: int, steps: list[dict]) -> float:
    """Diminishing returns within a day. steps e.g. [{upto:100,mult:1.0},...]."""
    for step in steps:
        upto = step.get("upto")
        if upto is None or correct_today < upto:
            return float(step.get("mult", 1.0))
    return 1.0


def answer_exp(
    level: str,
    response_sec: float,
    streak_after: int,
    correct_today: int,
    is_weekend: bool,
    cfg: dict,
) -> tuple[int, list[str]]:
    """EXP for one correct (scoring) answer. Returns (exp, bonus_names)."""
    base_table = cfg.get("base_by_level", BASE_EXP)
    exp = float(base_exp_for_level(level, base_table))
    names: list[str] = []
    sb = cfg.get("speed_bonus", {})
    if sb and response_sec <= float(sb.get("within_sec", 5)):
        exp *= 1.0 + float(sb.get("pct", 25)) / 100.0
        names.append("speed")
    for step in cfg.get("streak_bonus", []):
        if streak_after == int(step.get("n", 0)):
            exp += float(step.get("flat", 0))
            names.append(f"streak{step.get('n')}")
            break
    exp *= soft_cap_mult(correct_today, cfg.get("daily_soft_cap", []))
    if is_weekend and cfg.get("weekend_double"):
        exp *= 2.0
        names.append("weekend")
    return max(1, int(exp)), names


def session_win_exp(
    is_clean: bool, is_comeback: bool, is_giant_slay: bool, cfg: dict
) -> tuple[int, list[str]]:
    exp, names = 0, []
    if is_clean:
        exp += int(cfg.get("clean_session_win", {}).get("flat", 100))
        names.append("clean")
    if is_comeback:
        exp += int(cfg.get("comeback_win", {}).get("flat", 50))
        names.append("comeback")
    if is_giant_slay:
        exp += int(cfg.get("giant_slay_win", {}).get("flat", 50))
        names.append("giantslay")
    return exp, names


def gates_hold(gates: dict[str, int], per_level_correct: dict[str, int]) -> bool:
    return all(per_level_correct.get(lvl, 0) >= need for lvl, need in gates.items())


def accuracy_of(recent: list[dict], levels: list[str] | None = None) -> float | None:
    """recent: [{correct: bool, level: str}, ...] newest last. None if empty."""
    rows = [r for r in recent if not levels or r.get("level") in levels]
    if not rows:
        return None
    return sum(1 for r in rows if r.get("correct")) / len(rows)


def trial_holds(
    trial: dict,
    recent: list[dict],
    session_wins: int,
    best_n1_streak: int,
) -> bool:
    t = trial.get("type")
    if t == "accuracy_window":
        n = int(trial.get("n", 100))
        acc = accuracy_of(recent[-n:], trial.get("levels"))
        if acc is None or len([r for r in recent[-n:] if not trial.get("levels") or r.get("level") in trial["levels"]]) < n:
            return False
        return acc >= float(trial.get("min_acc", 1.0))
    if t == "session_wins":
        return session_wins >= int(trial.get("n", 1))
    if t == "n1_firstblood_streak":
        return best_n1_streak >= int(trial.get("n", 10))
    return False


def rank_index_for(
    exp: int,
    per_level_correct: dict[str, int],
    ranks_cfg: list[dict],
    recent: list[dict],
    session_wins: int,
    best_n1_streak: int,
) -> int:
    """Highest rank index whose threshold + gates + trials all hold."""
    idx = 0
    for i, rank in enumerate(ranks_cfg):
        if exp < int(rank.get("threshold", 0)):
            break
        if not gates_hold(rank.get("gates", {}) or {}, per_level_correct):
            break
        trials = rank.get("trials", []) or []
        if not all(trial_holds(t, recent, session_wins, best_n1_streak) for t in trials):
            break
        idx = i
    return idx


def is_weekend(now: dt.datetime | None = None) -> bool:
    return (now or dt.datetime.now()).weekday() >= 5


def lifetime_exp(current_season_exp: int, archived_exps: list[int], ceiling: int) -> int:
    return min(ceiling, current_season_exp + sum(archived_exps))
