"""Broad question categories (JLPT sections). Pure Python, no discord import.

There are exactly three categories — deliberately coarse so users pick in
one tap. The raw `instruction` strings in data/*.json vary a lot (spaces,
numbering), so classification works on normalized text (all spaces removed)
with ordered keyword rules, most specific first. data/*.json is never edited.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Category:
    id: str
    label: str  # bilingual, shown in Discord
    description: str  # English, shown as option description


CATEGORIES: list[Category] = [
    Category(
        id="vocab",
        label="Vocabulary • 語彙",
        description="Kanji reading, writing, meaning, paraphrase, usage",
    ),
    Category(
        id="grammar",
        label="Grammar • 文法",
        description="Fill-in-the-blank, ordering, cloze in passages",
    ),
    Category(
        id="reading",
        label="Reading • 読解",
        description="Comprehension, info search, A/B comparison",
    ),
]

BY_ID = {c.id: c for c in CATEGORIES}

ALL_TYPES = "ALL"
ALL_LABEL = "ALL types • すべての形式"


def _norm(text: str) -> str:
    return text.replace(" ", "").replace("　", "")


def classify(instruction: str) -> str:
    """Map one raw instruction string to a category id.

    Follows JLPT sectioning: numbered passage blanks (e.g. 19-23) count as
    grammar (文の文法), A/B comparison counts as reading.
    """
    s = _norm(instruction)

    # 1. Sentence ordering (star) — check first, it also contains 文.
    if "★" in instruction:
        return "grammar"

    # 2. Vocabulary: usage, paraphrase, meaning, reading, writing.
    if "つかいかた" in instruction or "使い方" in instruction:
        return "vocab"
    if "おなじいみ" in s or "同じ意味" in instruction:
        return "vocab"
    if "意味が最も近い" in s:
        return "vocab"
    if "読み方" in instruction or "ひらがなでどう" in s:
        return "vocab"
    if "漢字で書" in instruction or "ことばをどうか" in s or "ことばはどうか" in s or "どう書きますか" in s:
        return "vocab"

    # 3. Cloze: numbered blanks inside a passage (grammar in context).
    if (
        "文章全体" in instruction
        or "文章の意味" in instruction
        or "ぶんしょうのいみ" in s
        or "趣旨を踏まえて" in instruction
        or "19から" in s
        or "41から" in s
        or "48から" in s
        or "50から" in s
        or "14から" in s
        or "18から" in s
        or "(19)" in s
        or "(41)" in s
        or "(48)" in s
        or "(50)" in s
        or "(14)" in s
        or "(18)" in s
        or "[19]" in s
        or "[50]" in s
    ):
        return "grammar"

    # 4. A/B comparison passages.
    if "AとB" in s:
        return "reading"

    # 5. Grammar fill-in-the-blank (many spacing variants collapse here).
    if (
        "()に" in s
        or "に入れるのに最も" in s
        or "に何を入れますか" in s
        or "になにをいれますか" in s
    ):
        return "grammar"

    # 6. Reading comprehension / info search.
    if (
        "文章を読んで" in s
        or "文を読んで" in s
        or "ぶんしょうをよんで" in s
        or "案内" in instruction
        or "お知らせ" in instruction
        or "質問に答え" in s
        or "しつもんにこたえ" in s
        or "下の問い" in instruction
        or "下の質問" in instruction
        or "以下は" in instruction
        or instruction.strip() == "問題7"
    ):
        return "reading"

    # Safety net: never crash sampling on unseen wording.
    return "reading"
