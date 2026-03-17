"""Animals theme icons: bee, caterpillar, fish, butterfly."""

import math
from ..colors import C, HexColor
from . import register_theme, draw_star, draw_heart, draw_flower, draw_smiley


def draw_bee(c, cx, cy, s=1.0):
    sz = 14 * s
    c.setFillColor(C["yellow"])
    c.ellipse(cx - sz, cy - sz * 0.6, cx + sz, cy + sz * 0.6, fill=1, stroke=0)
    c.setFillColor(C["dark"])
    for i in range(-1, 2):
        c.rect(cx + i * sz * 0.35 - 2, cy - sz * 0.55, 4, sz * 1.1, fill=1, stroke=0)
    c.setFillColor(HexColor("#FFFFFFAA"))
    c.setStrokeColor(C["gray"])
    c.setLineWidth(0.5)
    c.ellipse(cx - sz * 0.5, cy + sz * 0.3, cx + 2, cy + sz * 1.2, fill=1, stroke=1)
    c.ellipse(cx - 2, cy + sz * 0.3, cx + sz * 0.5, cy + sz * 1.2, fill=1, stroke=1)
    c.setFillColor(C["white"])
    c.circle(cx + sz * 0.6, cy + sz * 0.15, 3 * s, fill=1, stroke=0)
    c.setFillColor(C["dark"])
    c.circle(cx + sz * 0.65, cy + sz * 0.15, 1.5 * s, fill=1, stroke=0)


def draw_caterpillar(c, cx, cy, s=1.0):
    cols = [C["green"], C["light_green"]] * 3
    for i in range(5):
        c.setFillColor(cols[i])
        c.circle(cx - i * 11 * s, cy, 9 * s, fill=1, stroke=0)
    c.setFillColor(C["orange"])
    c.circle(cx + 11 * s, cy, 10 * s, fill=1, stroke=0)
    c.setFillColor(C["white"])
    c.circle(cx + 8 * s, cy + 3.5 * s, 3 * s, fill=1, stroke=0)
    c.circle(cx + 14 * s, cy + 3.5 * s, 3 * s, fill=1, stroke=0)
    c.setFillColor(C["dark"])
    c.circle(cx + 8.5 * s, cy + 3.5 * s, 1.5 * s, fill=1, stroke=0)
    c.circle(cx + 14.5 * s, cy + 3.5 * s, 1.5 * s, fill=1, stroke=0)
    c.setStrokeColor(C["dark"])
    c.setLineWidth(1)
    c.line(cx + 9 * s, cy + 10 * s, cx + 5 * s, cy + 17 * s)
    c.line(cx + 13 * s, cy + 10 * s, cx + 17 * s, cy + 17 * s)
    c.setFillColor(C["orange"])
    c.circle(cx + 5 * s, cy + 17 * s, 2 * s, fill=1, stroke=0)
    c.circle(cx + 17 * s, cy + 17 * s, 2 * s, fill=1, stroke=0)


def draw_fish(c, cx, cy, s=1.0):
    c.setFillColor(C["blue"])
    p = c.beginPath()
    p.moveTo(cx + 15 * s, cy)
    p.lineTo(cx - 8 * s, cy + 10 * s)
    p.lineTo(cx - 8 * s, cy - 10 * s)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    c.ellipse(cx + 3 * s, cy - 10 * s, cx + 28 * s, cy + 10 * s, fill=1, stroke=0)
    c.setFillColor(C["white"])
    c.circle(cx + 20 * s, cy + 3 * s, 4 * s, fill=1, stroke=0)
    c.setFillColor(C["dark"])
    c.circle(cx + 21 * s, cy + 3 * s, 2 * s, fill=1, stroke=0)


def draw_butterfly(c, cx, cy, s=1.0):
    sz = 18 * s
    c.setFillColor(C["pink"])
    c.setStrokeColor(C["dark"])
    c.setLineWidth(0.5)
    c.ellipse(cx - sz, cy, cx - 2, cy + sz * 0.8, fill=1, stroke=1)
    c.ellipse(cx + 2, cy, cx + sz, cy + sz * 0.8, fill=1, stroke=1)
    c.ellipse(cx - sz * 0.7, cy - sz * 0.5, cx - 2, cy + 2, fill=1, stroke=1)
    c.ellipse(cx + 2, cy - sz * 0.5, cx + sz * 0.7, cy + 2, fill=1, stroke=1)
    c.setFillColor(C["dark"])
    c.ellipse(cx - 2, cy - sz * 0.3, cx + 2, cy + sz * 0.7, fill=1, stroke=0)
    c.setStrokeColor(C["dark"])
    c.setLineWidth(1)
    c.line(cx - 1, cy + sz * 0.65, cx - 5 * s, cy + sz)
    c.line(cx + 1, cy + sz * 0.65, cx + 5 * s, cy + sz)


# Animals theme color palette - warm, earthy, natural tones
animals_colors = {
    "backgrounds": [
        HexColor("#FFF9E6"),  # Soft cream
        HexColor("#FFF5D6"),  # Warm vanilla
        HexColor("#F0FFE6"),  # Light sage green
        HexColor("#FFE8CC"),  # Soft peach
        HexColor("#FFF0DB"),  # Pale wheat
    ],
    "banners": [
        C["orange"],      # Warm orange
        C["green"],       # Fresh green
        C["yellow"],      # Sunny yellow
        HexColor("#FFA07A"), # Light salmon
        C["light_green"], # Soft green
    ],
    "accents": [
        C["orange"],
        C["green"],
        C["yellow"],
        C["pink"],
        C["light_green"],
        C["teal"],
    ]
}

register_theme(
    "animals",
    start_icons=[draw_bee, draw_caterpillar, draw_fish],
    end_icons=[draw_butterfly, draw_flower, draw_star],
    shape_icons=[draw_smiley, draw_star, draw_flower, draw_heart, draw_butterfly, draw_bee],
    corner_icons=[draw_star, draw_heart, draw_flower],
    colors=animals_colors,
)
