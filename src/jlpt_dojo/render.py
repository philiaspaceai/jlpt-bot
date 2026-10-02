"""Profile card PNG rendering (WeasyPrint + PyMuPDF). No discord import.

Rank visual themes mirror design/profile-special.css section 1.
"""

from __future__ import annotations

import base64
from pathlib import Path
from string import Template

RANK_FILES = [
    "rank-01-houga.svg", "rank-02-reimei.svg", "rank-03-saku.svg",
    "rank-04-seikou.svg", "rank-05-meijin.svg", "rank-06-shinsei.svg",
    "rank-07-seikan.svg", "rank-08-ryuusei.svg", "rank-09-suisei.svg",
    "rank-10-shindan.svg",
]
BANNERS = {
    "meijin": "banner/meijin.jpeg", "shinsei": "banner/shinsei.jpeg",
    "seikan": "banner/seikan.jpeg", "ryuusei": "banner/ryuusei.jpeg",
    "suisei": "banner/suisei.jpeg", "shindan": "banner/shindan.jpeg",
}
NORMAL_ACCENTS = {
    "houga": ("#5DA24A", "#3E7A32"), "reimei": ("#D98A1F", "#A5660F"),
    "saku": ("#D95D87", "#A63A60"), "seikou": ("#4A90C4", "#2F6489"),
}
SPECIAL_VARS = {
    # Full var set per rank; mirrors the approved design themes.
    "meijin": ("--acc:#C9A227; --acc2:#E8C86A; --trim:#C9A227; --tt:#FFFFFF; "
               "--bg:#100D08; --pill:#1E1811; --pline:#3D3423; --bline:#4A3D24; --track:#2B241A; "
               "--ink:#FFFFFF; --muted:#9AA3C0; --sub:#C9D1E8; --foot:#6B7494; "
               "--tsh:rgba(0,0,0,0.9); --locked:#171208; --lockedline:#3A3122; --lockedtxt:#8A7F68; "
               "--nmc:#FFFFFF; --barbg:rgba(255,255,255,0.25);"),
    "shinsei": ("--acc:#2F6FED; --acc2:#8FC1E3; --trim:#F5C542; --tt:#F5C542; "
                "--bg:#0A1130; --pill:#161D45; --pline:#2C3768; --bline:#3A4678; --track:#232C5C; "
                "--ink:#FFFFFF; --muted:#9AA3C0; --sub:#C9D1E8; --foot:#6B7494; "
                "--tsh:rgba(0,0,0,0.9); --locked:#12173A; --lockedline:#2A3260; --lockedtxt:#6B7494; "
                "--nmc:#FFFFFF; --barbg:rgba(255,255,255,0.25);"),
    "seikan": ("--acc:#8A94A6; --acc2:#C0C8D8; --trim:#F5C542; --tt:#F5C542; "
               "--bg:#0A1130; --pill:#161D45; --pline:#2C3768; --bline:#3A4678; --track:#232C5C; "
               "--ink:#FFFFFF; --muted:#9AA3C0; --sub:#C9D1E8; --foot:#6B7494; "
               "--tsh:rgba(0,0,0,0.9); --locked:#12173A; --lockedline:#2A3260; --lockedtxt:#6B7494; "
               "--nmc:#FFFFFF; --barbg:rgba(255,255,255,0.25);"),
    "ryuusei": ("--acc:#4A90C4; --acc2:#8FC1E3; --trim:#4A90C4; --tt:#8FC1E3; "
                "--bg:#0A1130; --pill:#161D45; --pline:#2C3768; --bline:#3A4678; --track:#232C5C; "
                "--ink:#FFFFFF; --muted:#9AA3C0; --sub:#C9D1E8; --foot:#6B7494; "
                "--tsh:rgba(0,0,0,0.9); --locked:#12173A; --lockedline:#2A3260; --lockedtxt:#6B7494; "
                "--nmc:#FFFFFF; --barbg:rgba(255,255,255,0.25);"),
    "suisei": ("--acc:#59D6E6; --acc2:#8FE3F0; --trim:#F5C542; --tt:#F5C542; "
               "--bg:#0A1130; --pill:#161D45; --pline:#2C3768; --bline:#3A4678; --track:#232C5C; "
               "--ink:#FFFFFF; --muted:#9AA3C0; --sub:#C9D1E8; --foot:#6B7494; "
               "--tsh:rgba(0,0,0,0.9); --locked:#12173A; --lockedline:#2A3260; --lockedtxt:#6B7494; "
               "--nmc:#FFFFFF; --barbg:rgba(255,255,255,0.25);"),
    "shindan": ("--acc:#B98A12; --acc2:#E8C86A; --trim:#B98A12; --tt:#5A3D0C; --nmc:#3A2A10; "
                "--tsh:rgba(255,255,255,0.9); --bg:#FAF3E2; --pill:#FFFFFF; --pline:#E4C87E; "
                "--bline:#D9B45F; --track:#EFE0BC; --ink:#3A2A10; --muted:#8A7A52; --sub:#6B5D3A; "
                "--foot:#8A7A52; --locked:#F1E9D2; --lockedline:#D8C89A; --lockedtxt:#A89878; "
                "--barbg:rgba(58,42,16,0.18);"),
}
MONO_EXTRA = """
.scard.theme-MONO .sbp.rare { border-color: #6B5A2A; background: #221B0E; }
.scard.theme-MONO .sbp.epic { border-color: #8A6D1F; background: #26200F; }
.scard.theme-MONO .sbp.locked { background: #171208; border-color: #3A3122; }
.scard.theme-MONO .sbp.locked span { color: #8A7F68; }
"""
SHINDAN_EXTRA = """
.scard.theme-shindan .sbp.legendary { background: #F7ECD2; border-color: #D9B45F; }
"""
# Monochrome icon sets for earned badges: {theme: {badge_icon_base: themed_file}}.
# Locked states resolve via *-locked.svg existence checks in badge_icon().
MONO_ICONS = {
    "meijin": {"nightowl": "badge-nightowl-meijin.svg", "sharpshooter": "badge-sharpshooter-meijin.svg"},
    "shindan": {"nightowl": "badge-nightowl-shindan.svg", "sharpshooter": "badge-sharpshooter-shindan.svg",
                "unstoppable": "badge-unstoppable-shindan.svg", "giantslayer": "badge-giantslayer-shindan.svg",
                "perfectionist": "badge-perfectionist-shindan.svg"},
}


def _data_uri(png: bytes) -> str:
    return "data:image/png;base64," + base64.b64encode(png).decode()


def _fmt_num(n: int | float) -> str:
    if isinstance(n, float):
        return f"{n:.1f}" if n < 100 else f"{int(n):,}"
    return f"{n:,}"


def stat_pills(stats: list[tuple[str, int | float]], dark: bool) -> str:
    cls = "sppill" if dark else "npill"
    return "".join(
        f'<div class="{cls}"><div class="v"><b>{_fmt_num(v)}</b><span>{label}</span></div></div>'
        for label, v in stats)


def level_bars(levels: list[tuple[str, int]], dark: bool) -> str:
    cls = "slvl" if dark else "nlvl"
    peak = max([c for _, c in levels] or [1])
    out = []
    for lvl, count in levels:
        pct = round(100 * count / peak) if peak else 0
        out.append(f'<div class="{cls}"><i>{lvl}</i><div class="bar"><u style="width:{pct}%"></u></div>'
                   f"<b>{count:,}</b></div>")
    return "".join(out)


def badge_icon(badge_id: str, base_icon: str, rarity: str, locked: bool,
               theme: str, assets: Path) -> str:
    """Resolve themed icon file, falling back to defaults. Never raises."""
    if not locked:
        themed = MONO_ICONS.get(theme, {}).get(base_icon, "")
        if themed and (assets / themed).exists():
            return themed
        return f"badge-{base_icon}.svg"
    themed_locked = f"badge-{base_icon}-{theme}-locked.svg"
    if (assets / themed_locked).exists():
        return themed_locked
    return f"badge-{base_icon}-locked.svg"


def badge_pills(badges: list[dict], dark: bool) -> str:
    cls = "sbp" if dark else "nbp"
    out = []
    for b in badges:
        locked = b.get("locked", False)
        rarity = b.get("rarity", "common")
        extra = " locked" if locked else (f" {rarity}" if rarity != "common" else "")
        label = "???" if locked else b["name"]
        out.append(f'<div class="{cls}{extra}"><img src="{b["icon"]}" alt="">'
                   f"<span>{label}</span></div>")
    return "".join(out)


def profile_card(payload: dict, pkg_dir: str | Path) -> bytes:
    """Render a profile PNG. Payload keys: theme, rank{...}, name, initial,
    title, xp_cur, xp_max|None, xp_pct, xp_next|None, stats[(label,val)],
    levels[(lvl,count)], badges[{icon,name,rarity,locked}], badges_earned,
    badges_total, season_id, days_left, streak, lifetime, avatar_bytes|None,
    css_vars, banner, stars."""
    from weasyprint import HTML  # lazy: heavy import only when rendering
    import fitz

    pkg = Path(pkg_dir)
    assets = pkg / "assets"
    dark = payload["theme"] == "special"
    rank = payload["rank"]
    theme = rank["id"] if dark else ""
    extra = ""
    if theme == "meijin":
        extra = MONO_EXTRA.replace("MONO", "meijin")
    elif theme == "shindan":
        extra = SHINDAN_EXTRA

    avatar = payload.get("avatar_bytes")
    avatar_html = (f'<img class="avimg" src="{_data_uri(avatar)}" alt="">' if avatar
                   else payload.get("initial", "?"))
    if payload.get("xp_max"):
        xp_line = f"<b>{payload['xp_cur']:,}</b> / {payload['xp_max']:,} EXP"
        nxt = f"Next: {payload['xp_next']}" if payload.get("xp_next") else "Pinnacle reached"
    else:
        xp_line = f"<b>{payload['xp_cur']:,}</b> / MAX EXP"
        nxt = "Pinnacle reached"
    tpl_name = "profile_special.html" if dark else "profile_normal.html"
    tpl = Template((pkg / "templates" / tpl_name).read_text(encoding="utf-8"))
    card_class = f"scard theme-{theme}" if dark else "ncard"
    html = tpl.substitute(
        PAGE=payload["page_size"],
        CSS_VARS=payload.get("css_vars", ""),
        EXTRA_CSS=extra,
        BANNER=payload.get("banner") or "",
        STARS=payload.get("stars", ""),
        RANK_ICON=rank["icon"],
        AVATAR=avatar_html,
        NAME=payload["name"],
        TITLE=payload.get("title", ""),
        RANK_LINE=f"{rank['en']} {rank['ja']}",
        RANK_NO=f"RANK {rank['index'] + 1} / 10",
        CARD_CLASS=card_class,
        XP_LINE=xp_line,
        XP_PCT=payload.get("xp_pct", 0),
        XP_NEXT=nxt,
        STATS=stat_pills(payload["stats"], dark),
        LEVELS=level_bars(payload["levels"], dark),
        BADGES=badge_pills(payload["badges"], dark),
        BADGE_COUNT=f"{payload.get('badges_earned', 0)} of {payload.get('badges_total', 0)}",
        SEASON_ID=payload.get("season_id", 1),
        DAYS_LEFT=payload.get("days_left", 0),
        STREAK=payload.get("streak", 0),
        LIFETIME=f"{payload.get('lifetime', 0):,}",
    )
    pdf = HTML(string=html, base_url=str(assets) + "/").write_pdf(target=None)
    doc = fitz.open(stream=pdf, filetype="pdf")
    pg = doc[0]
    pix = pg.get_pixmap(matrix=fitz.Matrix(1280 / pg.rect.width, 1280 / pg.rect.width))
    return pix.tobytes("png")
