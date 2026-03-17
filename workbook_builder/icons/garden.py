"""Garden theme icons: ladybug, snail, worm, mushroom, leaf."""

import math
from ..colors import C, HexColor
from . import register_theme, draw_flower, draw_heart


def draw_ladybug(c, cx, cy, s=1.0):
    c.setFillColor(C["red"])
    c.circle(cx, cy, 12 * s, fill=1, stroke=0)
    c.setStrokeColor(C["dark"])
    c.setLineWidth(1.5 * s)
    c.line(cx, cy - 12 * s, cx, cy + 12 * s)
    c.setFillColor(C["dark"])
    c.circle(cx, cy + 14 * s, 6 * s, fill=1, stroke=0)
    c.circle(cx - 5 * s, cy + 4 * s, 2.5 * s, fill=1, stroke=0)
    c.circle(cx + 5 * s, cy + 4 * s, 2.5 * s, fill=1, stroke=0)
    c.circle(cx - 4 * s, cy - 4 * s, 2 * s, fill=1, stroke=0)
    c.circle(cx + 4 * s, cy - 4 * s, 2 * s, fill=1, stroke=0)
    c.setStrokeColor(C["dark"])
    c.setLineWidth(1)
    c.line(cx - 3 * s, cy + 18 * s, cx - 7 * s, cy + 22 * s)
    c.line(cx + 3 * s, cy + 18 * s, cx + 7 * s, cy + 22 * s)


def draw_snail(c, cx, cy, s=1.0):
    c.setFillColor(HexColor("#DEB887"))
    c.ellipse(cx - 16 * s, cy - 6 * s, cx + 4 * s, cy + 4 * s, fill=1, stroke=0)
    c.setFillColor(C["orange"])
    c.circle(cx + 2 * s, cy + 2 * s, 12 * s, fill=1, stroke=0)
    c.setStrokeColor(HexColor("#D2691E"))
    c.setLineWidth(1.5 * s)
    c.circle(cx + 2 * s, cy + 2 * s, 8 * s, fill=0, stroke=1)
    c.circle(cx + 2 * s, cy + 2 * s, 4 * s, fill=0, stroke=1)
    c.setStrokeColor(HexColor("#DEB887"))
    c.setLineWidth(1.5 * s)
    c.line(cx - 10 * s, cy + 2 * s, cx - 12 * s, cy + 10 * s)
    c.line(cx - 6 * s, cy + 2 * s, cx - 4 * s, cy + 10 * s)
    c.setFillColor(C["dark"])
    c.circle(cx - 12 * s, cy + 10 * s, 1.5 * s, fill=1, stroke=0)
    c.circle(cx - 4 * s, cy + 10 * s, 1.5 * s, fill=1, stroke=0)


def draw_worm(c, cx, cy, s=1.0):
    c.setStrokeColor(C["pink"])
    c.setLineWidth(6 * s)
    c.setLineCap(1)
    p = c.beginPath()
    p.moveTo(cx - 18 * s, cy)
    p.curveTo(cx - 10 * s, cy + 10 * s, cx - 2 * s, cy - 10 * s, cx + 8 * s, cy)
    p.curveTo(cx + 12 * s, cy + 5 * s, cx + 16 * s, cy + 3 * s, cx + 18 * s, cy)
    c.drawPath(p, fill=0, stroke=1)
    c.setLineCap(0)
    c.setFillColor(C["pink"])
    c.circle(cx + 18 * s, cy, 6 * s, fill=1, stroke=0)
    c.setFillColor(C["white"])
    c.circle(cx + 17 * s, cy + 2 * s, 2 * s, fill=1, stroke=0)
    c.circle(cx + 21 * s, cy + 2 * s, 2 * s, fill=1, stroke=0)
    c.setFillColor(C["dark"])
    c.circle(cx + 17.5 * s, cy + 2 * s, 1 * s, fill=1, stroke=0)
    c.circle(cx + 21.5 * s, cy + 2 * s, 1 * s, fill=1, stroke=0)


def draw_mushroom(c, cx, cy, s=1.0):
    c.setFillColor(HexColor("#F5DEB3"))
    c.rect(cx - 5 * s, cy - 14 * s, 10 * s, 16 * s, fill=1, stroke=0)
    c.setFillColor(C["red"])
    p = c.beginPath()
    p.moveTo(cx - 16 * s, cy + 2 * s)
    for i in range(0, 181, 5):
        rad = math.radians(i)
        p.lineTo(cx + 16 * s * math.cos(rad), cy + 2 * s + 14 * s * math.sin(rad))
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    c.setFillColor(C["white"])
    c.circle(cx - 6 * s, cy + 10 * s, 2.5 * s, fill=1, stroke=0)
    c.circle(cx + 5 * s, cy + 12 * s, 2 * s, fill=1, stroke=0)
    c.circle(cx, cy + 6 * s, 1.5 * s, fill=1, stroke=0)


def draw_leaf(c, cx, cy, s=1.0):
    c.setFillColor(C["green"])
    p = c.beginPath()
    p.moveTo(cx - 14 * s, cy)
    p.curveTo(cx - 8 * s, cy + 14 * s, cx + 8 * s, cy + 14 * s, cx + 14 * s, cy)
    p.curveTo(cx + 8 * s, cy - 14 * s, cx - 8 * s, cy - 14 * s, cx - 14 * s, cy)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    c.setStrokeColor(C["light_green"])
    c.setLineWidth(1.5 * s)
    c.line(cx - 12 * s, cy, cx + 12 * s, cy)
    c.line(cx - 2 * s, cy, cx - 6 * s, cy + 6 * s)
    c.line(cx + 2 * s, cy, cx + 6 * s, cy - 6 * s)


# Garden theme color palette - fresh greens and floral tones
garden_colors = {
    "backgrounds": [
        HexColor("#F0FFF4"),  # Mint cream
        HexColor("#E8F5E9"),  # Soft mint
        HexColor("#FFF0F8"),  # Pale rose
        HexColor("#F1F8E9"),  # Light lime
        HexColor("#E8F8F5"),  # Pale turquoise
    ],
    "banners": [
        C["green"],       # Fresh green
        HexColor("#66BB6A"),  # Medium green
        C["pink"],        # Floral pink
        C["light_green"], # Soft green
        HexColor("#81C784"),  # Light green
    ],
    "accents": [
        C["green"],
        C["pink"],
        C["light_green"],
        C["purple"],
        HexColor("#66BB6A"),  # Medium green
        C["orange"],
    ]
}

register_theme(
    "garden",
    start_icons=[draw_ladybug, draw_snail, draw_worm],
    end_icons=[draw_flower, draw_mushroom, draw_leaf],
    shape_icons=[draw_flower, draw_mushroom, draw_leaf, draw_ladybug, draw_snail, draw_heart],
    corner_icons=[draw_flower, draw_leaf, draw_heart],
    colors=garden_colors,
)
