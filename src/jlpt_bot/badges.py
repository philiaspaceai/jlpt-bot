"""Badge condition engine. Pure Python; storage lives in db.py."""

from __future__ import annotations

from .progression import accuracy_of


def check_badges(
    badges_cfg: list[dict],
    snapshot: dict,
    recent: list[dict],
    event: dict | None = None,
) -> list[str]:
    """Return badge ids whose conditions hold. Caller awards + equips via db."""
    event = event or {}
    earned: list[str] = []
    for badge in badges_cfg:
        cond = badge.get("cond", {})
        t = cond.get("type")
        ok = False
        if t == "first_bloods":
            ok = int(snapshot.get("first_bloods", 0)) >= int(cond.get("n", 1))
        elif t == "best_streak":
            ok = int(snapshot.get("best_streak", 0)) >= int(cond.get("n", 1))
        elif t == "mistakes_total":
            ok = int(snapshot.get("mistakes", 0)) >= int(cond.get("n", 1))
        elif t == "clean_sessions":
            ok = int(snapshot.get("clean_sessions", 0)) >= int(cond.get("n", 1))
        elif t == "session_wins":
            ok = int(snapshot.get("wins", 0)) >= int(cond.get("n", 1))
        elif t == "giant_slays":
            ok = int(snapshot.get("giant_slays", 0)) >= int(cond.get("n", 1))
        elif t == "accuracy_window":
            n = int(cond.get("n", 20))
            window = recent[-n:]
            if len(window) >= n:
                acc = accuracy_of(window)
                ok = acc is not None and acc >= float(cond.get("min_acc", 1.0))
        elif t == "night_owl":
            ok = 0 <= int(event.get("hour", -1)) < 4
        elif t == "early_bird":
            ok = bool(event.get("early_bird"))
        if ok:
            earned.append(str(badge.get("id")))
    return earned
