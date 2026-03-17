"""Food theme icons: apple, cherry, cupcake, ice cream, cookie, lollipop."""

from ..colors import C, HexColor
from . import register_theme


def draw_apple(c, cx, cy, s=1.0):
    c.setFillColor(C["red"])
    c.circle(cx - 4 * s, cy, 10 * s, fill=1, stroke=0)
    c.circle(cx + 4 * s, cy, 10 * s, fill=1, stroke=0)
    c.setStrokeColor(HexColor("#8B4513"))
    c.setLineWidth(2 * s)
    c.line(cx, cy + 8 * s, cx + 2 * s, cy + 14 * s)
    c.setFillColor(C["green"])
    p = c.beginPath()
    p.moveTo(cx + 2 * s, cy + 13 * s)
    p.curveTo(cx + 8 * s, cy + 16 * s, cx + 10 * s, cy + 12 * s, cx + 6 * s, cy + 10 * s)
    p.close()
    c.drawPath(p, fill=1, stroke=0)


def draw_cherry(c, cx, cy, s=1.0):
    c.setFillColor(C["red"])
    c.circle(cx - 6 * s, cy - 4 * s, 7 * s, fill=1, stroke=0)
    c.circle(cx + 6 * s, cy - 4 * s, 7 * s, fill=1, stroke=0)
    c.setStrokeColor(C["green"])
    c.setLineWidth(1.5 * s)
    c.line(cx - 6 * s, cy + 3 * s, cx, cy + 14 * s)
    c.line(cx + 6 * s, cy + 3 * s, cx, cy + 14 * s)
    c.setFillColor(C["green"])
    p = c.beginPath()
    p.moveTo(cx, cy + 14 * s)
    p.curveTo(cx + 6 * s, cy + 18 * s, cx + 10 * s, cy + 14 * s, cx + 6 * s, cy + 11 * s)
    p.close()
    c.drawPath(p, fill=1, stroke=0)


def draw_cupcake(c, cx, cy, s=1.0):
    c.setFillColor(C["pink"])
    p = c.beginPath()
    p.moveTo(cx - 10 * s, cy)
    p.lineTo(cx - 7 * s, cy - 14 * s)
    p.lineTo(cx + 7 * s, cy - 14 * s)
    p.lineTo(cx + 10 * s, cy)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    c.setFillColor(HexColor("#FFB6C1"))
    p = c.beginPath()
    p.moveTo(cx - 12 * s, cy)
    p.curveTo(cx - 8 * s, cy + 12 * s, cx + 8 * s, cy + 12 * s, cx + 12 * s, cy)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    c.setFillColor(C["red"])
    c.circle(cx, cy + 10 * s, 3 * s, fill=1, stroke=0)


def draw_icecream(c, cx, cy, s=1.0):
    c.setFillColor(HexColor("#DEB887"))
    p = c.beginPath()
    p.moveTo(cx - 10 * s, cy)
    p.lineTo(cx, cy - 18 * s)
    p.lineTo(cx + 10 * s, cy)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    c.setFillColor(C["pink"])
    c.circle(cx, cy + 4 * s, 10 * s, fill=1, stroke=0)
    c.setFillColor(HexColor("#F5DEB3"))
    c.circle(cx - 5 * s, cy + 12 * s, 7 * s, fill=1, stroke=0)
    c.setFillColor(HexColor("#8B4513"))
    c.circle(cx + 5 * s, cy + 12 * s, 7 * s, fill=1, stroke=0)


def draw_cookie(c, cx, cy, s=1.0):
    c.setFillColor(HexColor("#D2A060"))
    c.circle(cx, cy, 12 * s, fill=1, stroke=0)
    c.setFillColor(HexColor("#5C3317"))
    for dx, dy, r in [(-4, 4, 2), (5, 2, 2.5), (-2, -4, 2), (3, -6, 1.8), (-6, -2, 1.5)]:
        c.circle(cx + dx * s, cy + dy * s, r * s, fill=1, stroke=0)


def draw_lollipop(c, cx, cy, s=1.0):
    c.setStrokeColor(HexColor("#DEB887"))
    c.setLineWidth(3 * s)
    c.line(cx, cy - 14 * s, cx, cy + 2 * s)
    c.setFillColor(C["red"])
    c.circle(cx, cy + 10 * s, 10 * s, fill=1, stroke=0)
    c.setStrokeColor(C["white"])
    c.setLineWidth(1.5 * s)
    c.circle(cx, cy + 10 * s, 5 * s, fill=0, stroke=1)
    c.circle(cx, cy + 10 * s, 2 * s, fill=0, stroke=1)


# Food theme color palette - warm, appetizing, and fun colors
food_colors = {
    "backgrounds": [
        HexColor("#FFF5E6"),  # Cream
        HexColor("#FFEBEE"),  # Light pink
        HexColor("#FFF9E6"),  # Soft butter
        HexColor("#FFE5E0"),  # Peach cream
        HexColor("#F0FFF0"),  # Mint cream
    ],
    "banners": [
        HexColor("#FF7043"),  # Warm coral
        C["pink"],        # Pink frosting
        C["yellow"],      # Butter yellow
        HexColor("#FF6F61"),  # Coral
        HexColor("#FFB74D"),  # Warm orange
    ],
    "accents": [
        C["red"],
        C["pink"],
        C["orange"],
        C["yellow"],
        HexColor("#FF6F61"),  # Coral
        HexColor("#8BC34A"),  # Lime green
    ]
}

register_theme(
    "food",
    start_icons=[draw_apple, draw_cherry, draw_cupcake],
    end_icons=[draw_icecream, draw_cookie, draw_lollipop],
    shape_icons=[draw_apple, draw_cookie, draw_cupcake, draw_icecream, draw_cherry, draw_lollipop],
    corner_icons=[draw_apple, draw_cookie, draw_cherry],
    colors=food_colors,
)
