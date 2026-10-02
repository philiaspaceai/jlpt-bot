"""Plain data models. No discord import allowed here."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Question:
    id: int
    level: str  # N5..N1
    instruction: str
    passage: str | None
    stem: str
    target: str | None
    options: list[str]  # original order, length 4
    answer: int  # 1..4 in original order
    correct_order: list[int] | None = None


@dataclass(frozen=True)
class ShuffledQuestion:
    """One question instance with display-order options.

    Anti pattern-recognition: options are shuffled per session and the
    correct index is remapped. The original order is never sent to Discord.
    """

    source: Question
    displayed_options: list[str]  # length 4, shuffled
    displayed_answer: int  # 1..4 in displayed order


@dataclass
class QuizConfig:
    level: str  # N5..N1 or ALL
    type_id: str  # type group id or ALL
    type_label: str  # human readable instruction (or ALL)
    count: int
    starter_id: int
    starter_name: str
    guild_id: int
    channel_id: int


@dataclass
class PlayerScore:
    user_id: int
    display_name: str
    points: int = 0

