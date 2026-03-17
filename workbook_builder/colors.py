"""Color constants, palettes, and rotation helpers."""

from reportlab.lib.colors import HexColor

# ── Core palette ──────────────────────────────────────────────────────

C = {
    "pink": HexColor("#FF6B9D"),
    "orange": HexColor("#FF9A56"),
    "blue": HexColor("#5BC0EB"),
    "green": HexColor("#6BCB77"),
    "purple": HexColor("#B47EDE"),
    "yellow": HexColor("#FFD93D"),
    "red": HexColor("#E85D5D"),
    "teal": HexColor("#45B7AA"),
    "gray": HexColor("#D8D8D8"),
    "dark": HexColor("#555555"),
    "white": HexColor("#FFFFFF"),
    "light_green": HexColor("#8BD98B"),
}

# ── Page backgrounds ──────────────────────────────────────────────────

BG = {
    "cream": HexColor("#FFF9F0"),
    "blue": HexColor("#E8F6FD"),
    "pink": HexColor("#FFF0F5"),
    "green": HexColor("#F0FFF0"),
    "purple": HexColor("#F5F0FF"),
    "orange": HexColor("#FFF5EB"),
    "yellow": HexColor("#FFFDE8"),
}

# ── Rotating lists for variety across pages ───────────────────────────

ACCENT_COLORS = [C["pink"], C["blue"], C["green"], C["purple"], C["orange"], C["teal"], C["red"]]
BG_LIST = [BG["yellow"], BG["blue"], BG["green"], BG["pink"], BG["purple"], BG["orange"], BG["cream"]]
BANNER_COLORS = [C["blue"], C["green"], C["purple"], C["pink"], C["orange"], C["teal"], C["red"]]

ENCOURAGEMENTS = [
    "Great job! Keep up the awesome tracing!",
    "You're a superstar! Amazing work!",
    "Fantastic tracing! You're getting so good!",
    "Wow, look at you go! Brilliant!",
    "Keep it up! You're doing wonderfully!",
    "You're a tracing champion!",
    "Beautiful work! So proud of you!",
]


def get_accent(page_idx, row=0, theme=None):
    """Get a rotating accent color based on page and row index, optionally theme-specific."""
    if theme and "colors" in theme and "accents" in theme["colors"]:
        accent_list = theme["colors"]["accents"]
        return accent_list[(page_idx * 3 + row) % len(accent_list)]
    return ACCENT_COLORS[(page_idx * 3 + row) % len(ACCENT_COLORS)]


def get_bg(page_idx, theme=None):
    """Get a rotating background color, optionally theme-specific."""
    if theme and "colors" in theme and "backgrounds" in theme["colors"]:
        bg_list = theme["colors"]["backgrounds"]
        return bg_list[page_idx % len(bg_list)]
    return BG_LIST[page_idx % len(BG_LIST)]


def get_banner(page_idx, theme=None):
    """Get a rotating banner color, optionally theme-specific."""
    if theme and "colors" in theme and "banners" in theme["colors"]:
        banner_list = theme["colors"]["banners"]
        return banner_list[page_idx % len(banner_list)]
    return BANNER_COLORS[page_idx % len(BANNER_COLORS)]


def get_encouragement(page_idx):
    """Get a rotating encouragement message."""
    return ENCOURAGEMENTS[page_idx % len(ENCOURAGEMENTS)]


# ── Guide-line dash patterns ──────────────────────────────────────────

DASH_STYLES = {
    "dashed": (8, 6),
    "dotted": (3, 4),
    "solid": ([], 0),
}


def parse_dash_style(style):
    """Convert a style name to a (dash, gap) tuple for reportlab."""
    return DASH_STYLES.get(style, (8, 6))
