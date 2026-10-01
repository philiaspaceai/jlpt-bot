"""Render smoke tests: both templates produce valid PNG bytes."""

from pathlib import Path

from jlpt_bot.render import RANK_FILES, badge_icon, profile_card

PKG = Path("src/jlpt_bot")
ASSETS = PKG / "assets"


def _payload(theme: str, rank_idx: int) -> dict:
    rank_id = ["houga", "reimei", "saku", "seikou", "meijin", "shinsei",
               "seikan", "ryuusei", "suisei", "shindan"][rank_idx]
    names = ["Houga", "Reimei", "Saku", "Seikou", "Meijin", "Shinsei",
             "Seikan", "Ryuusei", "Suisei", "Shindan"]
    ja = ["萌芽", "黎明", "咲", "星光", "名人", "新星", "星冠", "流星", "彗星", "神断"]
    from jlpt_bot.render import BANNERS  # noqa: verify export surface
    return {
        "theme": theme,
        "rank": {"id": rank_id, "en": names[rank_idx], "ja": ja[rank_idx],
                 "index": rank_idx, "icon": RANK_FILES[rank_idx]},
        "name": "T", "initial": "T", "title": "Tester",
        "xp_cur": 100, "xp_max": 2000, "xp_pct": 5, "xp_next": "Reimei 黎明",
        "stats": [(f"s{i}", i) for i in range(12)],
        "levels": [(lvl, i * 10) for i, lvl in enumerate(["N5", "N4", "N3", "N2", "N1"])],
        "badges": [{"icon": badge_icon("firstblood", "drop", "common", False, rank_id, ASSETS),
                    "name": "First Blood", "rarity": "common", "locked": False}],
        "badges_earned": 1, "badges_total": 10, "season_id": 1, "days_left": 30,
        "streak": 1, "lifetime": 100,
        "css_vars": "--acc:#5DA24A; --deep:#3E7A32;" if theme == "normal" else "",
        "banner": {"ryuusei": "banner/ryuusei.jpeg"}.get(rank_id, ""),
        "stars": "", "page_size": "1280px 720px" if theme == "normal" else "1280px 980px",
    }


def _is_png(data: bytes) -> bool:
    return data[:8] == b"\x89PNG\r\n\x1a\n"


def test_render_normal_card():
    png = profile_card(_payload("normal", 2), PKG)
    assert _is_png(png) and len(png) > 50_000


def test_render_special_card():
    png = profile_card(_payload("special", 7), PKG)
    assert _is_png(png) and len(png) > 50_000


def test_badge_icon_fallbacks():
    assert badge_icon("x", "nope", "common", False, "houga", ASSETS) == "badge-nope.svg"
    assert badge_icon("nightowl", "nightowl", "rare", False, "meijin", ASSETS) == "badge-nightowl-meijin.svg"
    assert badge_icon("unstoppable", "unstoppable", "epic", True, "meijin", ASSETS) == "badge-unstoppable-meijin-locked.svg"
    assert badge_icon("nightowl", "nightowl", "rare", True, "houga", ASSETS) == "badge-nightowl-locked.svg"
