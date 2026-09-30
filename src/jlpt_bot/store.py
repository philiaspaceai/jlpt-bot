"""Question loading, broad-category filtering, sampling, option shuffling.

Pure Python module. No discord import allowed here so the quiz core
stays testable without a Discord connection.
"""

from __future__ import annotations

import json
import random
from pathlib import Path

from . import categories
from .models import Question, ShuffledQuestion

LEVELS = ["N5", "N4", "N3", "N2", "N1"]
ALL_LEVELS = "ALL"
ALL_TYPES = categories.ALL_TYPES
COUNT_CHOICES = [5, 10, 15, 20]


class QuestionStore:
    def __init__(self, questions_by_level: dict[str, list[Question]]) -> None:
        self._by_level = {lvl: list(qs) for lvl, qs in questions_by_level.items()}

    @classmethod
    def load(cls, data_dir: str | Path) -> QuestionStore:
        base = Path(data_dir)
        by_level: dict[str, list[Question]] = {}
        for level in LEVELS:
            path = base / f"{level}.json"
            if not path.exists():
                by_level[level] = []
                continue
            raw = json.loads(path.read_text(encoding="utf-8"))
            questions: list[Question] = []
            for item in raw:
                options = list(item.get("options") or [])
                if len(options) != 4:
                    continue
                answer = int(item.get("answer", 1))
                if answer < 1 or answer > 4:
                    continue
                questions.append(
                    Question(
                        id=int(item.get("id", 0)),
                        level=level,
                        instruction=str(item.get("instruction") or ""),
                        passage=item.get("passage"),
                        stem=str(item.get("stem") or ""),
                        target=item.get("target"),
                        options=[str(o) for o in options],
                        answer=answer,
                        correct_order=item.get("correctOrder"),
                    )
                )
            by_level[level] = questions
        return cls(by_level)

    def levels(self) -> list[str]:
        return [lvl for lvl in LEVELS if self._by_level.get(lvl)]

    def total(self, level: str) -> int:
        if level == ALL_LEVELS:
            return sum(len(v) for v in self._by_level.values())
        return len(self._by_level.get(level, []))

    def _pool(self, level: str, category_id: str) -> list[Question]:
        if level == ALL_LEVELS:
            pool: list[Question] = []
            for lvl in LEVELS:
                pool.extend(self._by_level.get(lvl, []))
        else:
            pool = list(self._by_level.get(level, []))
        if category_id == ALL_TYPES or not category_id:
            return pool
        return [q for q in pool if categories.classify(q.instruction) == category_id]

    def category_counts(self, level: str) -> dict[str, int]:
        """Count questions per broad category; zero-count categories omitted."""
        counts: dict[str, int] = {}
        for q in self._pool(level, ALL_TYPES):
            cat = categories.classify(q.instruction)
            counts[cat] = counts.get(cat, 0) + 1
        return counts

    def sample(self, level: str, category_id: str, count: int, rng: random.Random) -> list[Question]:
        pool = self._pool(level, category_id)
        if not pool:
            return []
        count = max(1, min(count, len(pool)))
        return rng.sample(pool, count)


def shuffle_options(question: Question, rng: random.Random) -> ShuffledQuestion:
    """Shuffle display order and remap the correct answer.

    This is the anti pattern-recognition measure: the same question shows
    different option positions in every session.
    """
    order = [0, 1, 2, 3]
    rng.shuffle(order)
    displayed = [question.options[i] for i in order]
    # original correct index (0-based) -> new position
    original_correct = question.answer - 1
    displayed_answer = order.index(original_correct) + 1
    return ShuffledQuestion(
        source=question,
        displayed_options=displayed,
        displayed_answer=displayed_answer,
    )
