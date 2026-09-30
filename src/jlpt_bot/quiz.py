"""Single-session quiz state machine. Pure Python, no discord import.

Rules (locked by user answers):
- Only one QuizSession may be active per process (enforced by QuizManager).
- Fastest finger wins: the first correct answer scores +1 and advances.
- Wrong answers are ignored (no broadcast).
- Stale presses for an old question index are ignored.
"""

from __future__ import annotations

import asyncio
import time
import uuid
from dataclasses import dataclass, field

from .models import AnswerResult, PlayerScore, QuizConfig, ShuffledQuestion


@dataclass
class QuizSession:
    config: QuizConfig
    questions: list[ShuffledQuestion]
    session_id: str = field(default_factory=lambda: uuid.uuid4().hex[:8])
    current_index: int = 0
    scores: dict[int, PlayerScore] = field(default_factory=dict)
    active: bool = True
    last_correct_id: int | None = None
    last_correct_name: str | None = None
    last_activity: float = field(default_factory=time.time)
    message_id: int | None = None
    _lock: asyncio.Lock = field(default_factory=asyncio.Lock, repr=False)

    @property
    def total(self) -> int:
        return len(self.questions)

    def current(self) -> ShuffledQuestion | None:
        if not self.active:
            return None
        if 0 <= self.current_index < len(self.questions):
            return self.questions[self.current_index]
        return None

    def is_finished(self) -> bool:
        return self.current_index >= len(self.questions)

    def touch(self) -> None:
        self.last_activity = time.time()

    def idle_seconds(self) -> float:
        return time.time() - self.last_activity

    async def answer(
        self, user_id: int, display_name: str, picked: int, question_index: int
    ) -> AnswerResult:
        """Record an answer. Thread-safe via asyncio lock."""
        async with self._lock:
            if not self.active or self.is_finished():
                return AnswerResult(kind="finished")
            if question_index != self.current_index:
                return AnswerResult(kind="stale")
            current = self.questions[self.current_index]
            if picked == current.displayed_answer:
                entry = self.scores.get(user_id)
                if entry is None:
                    entry = PlayerScore(user_id=user_id, display_name=display_name, points=0)
                    self.scores[user_id] = entry
                entry.display_name = display_name
                entry.points += 1
                self.last_correct_id = user_id
                self.last_correct_name = display_name
                self.current_index += 1
                self.touch()
                return AnswerResult(kind="correct", scorer_id=user_id, scorer_name=display_name)
            self.touch()
            return AnswerResult(kind="wrong")

    def advance_on_timeout(self) -> bool:
        """Advance without scoring (reserved for future per-question timeout)."""
        if not self.active or self.is_finished():
            return False
        self.current_index += 1
        self.touch()
        return True

    def leaderboard(self) -> list[PlayerScore]:
        return sorted(self.scores.values(), key=lambda s: (-s.points, s.display_name.lower()))

    def close(self) -> None:
        self.active = False
        self.touch()

    def can_stop(self, user_id: int, is_admin: bool) -> bool:
        return user_id == self.config.starter_id or is_admin


class QuizManager:
    """Enforces at most one active session. Blast-radius boundary for state."""

    def __init__(self) -> None:
        self._session: QuizSession | None = None
        self._lock = asyncio.Lock()

    async def start(self, config: QuizConfig, questions: list[ShuffledQuestion]) -> QuizSession | None:
        async with self._lock:
            if self._session is not None and self._session.active:
                return None
            session = QuizSession(config=config, questions=questions)
            self._session = session
            return session

    async def get(self) -> QuizSession | None:
        async with self._lock:
            sess = self._session
            if sess is not None and sess.active:
                return sess
            return None

    async def get_any(self) -> QuizSession | None:
        async with self._lock:
            return self._session

    async def stop(self) -> QuizSession | None:
        async with self._lock:
            sess = self._session
            if sess is not None:
                sess.close()
            self._session = None
            return sess

    async def clear_finished(self) -> None:
        async with self._lock:
            sess = self._session
            if sess is not None and (not sess.active or sess.is_finished()):
                self._session = None
