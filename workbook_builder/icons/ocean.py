"""Ocean theme icons: whale, turtle, shell, starfish, coral."""

import math
from ..colors import C, HexColor
from . import register_theme, draw_star, draw_heart
from .animals import draw_fish


def draw_whale(c, cx, cy, s=1.0):
    c.setFillColor(C["blue"])
    c.ellipse(cx - 16 * s, cy - 10 * s, cx + 16 * s, cy + 8 * s, fill=1, stroke=0)
    p = c.beginPath()
    p.moveTo(cx - 16 * s, cy - 2 * s)
    p.lineTo(cx - 26 * s, cy - 10 * s)
    p.lineTo(cx - 26 * s, cy + 6 * s)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    c.setFillColor(C["white"])
    c.circle(cx + 8 * s, cy + 1 * s, 3 * s, fill=1, stroke=0)
    c.setFillColor(C["dark"])
    c.circle(cx + 8.5 * s, cy + 1 * s, 1.5 * s, fill=1, stroke=0)
    c.setStrokeColor(C["blue"])
    c.setLineWidth(1.5 * s)
    c.line(cx + 4 * s, cy + 8 * s, cx + 2 * s, cy + 14 * s)
    c.line(cx + 4 * s, cy + 8 * s, cx + 6 * s, cy + 14 * s)


def draw_turtle(c, cx, cy, s=1.0):
    c.setFillColor(C["green"])
    c.ellipse(cx - 12 * s, cy - 8 * s, cx + 12 * s, cy + 8 * s, fill=1, stroke=0)
    c.setStrokeColor(C["light_green"])
    c.setLineWidth(1)
    c.line(cx - 6 * s, cy - 6 * s, cx - 6 * s, cy + 6 * s)
    c.line(cx + 6 * s, cy - 6 * s, cx + 6 * s, cy + 6 * s)
    c.setFillColor(C["light_green"])
    c.circle(cx + 16 * s, cy, 5 * s, fill=1, stroke=0)
    c.setFillColor(C["dark"])
    c.circle(cx + 17.5 * s, cy + 1 * s, 1.2 * s, fill=1, stroke=0)
    c.setFillColor(C["light_green"])
    for dx, dy in [(-8, -9), (-8, 9), (6, -9), (6, 9)]:
        c.ellipse(cx + dx * s - 3 * s, cy + dy * s - 2 * s,
                  cx + dx * s + 3 * s, cy + dy * s + 2 * s, fill=1, stroke=0)


def draw_shell(c, cx, cy, s=1.0):
    c.setStrokeColor(C["orange"])
    c.setFillColor(HexColor("#FFE4B5"))
    c.setLineWidth(1.5 * s)
    p = c.beginPath()
    p.moveTo(cx, cy - 12 * s)
    for i in range(0, 181, 5):
        rad = math.radians(i)
        p.lineTo(cx + 14 * s * math.cos(rad), cy - 12 * s + 14 * s * math.sin(rad))
    p.close()
    c.drawPath(p, fill=1, stroke=1)
    c.setStrokeColor(C["orange"])
    c.setLineWidth(0.8 * s)
    for angle in [30, 60, 90, 120, 150]:
        rad = math.radians(angle)
        c.line(cx, cy - 12 * s, cx + 12 * s * math.cos(rad), cy - 12 * s + 12 * s * math.sin(rad))


def draw_starfish(c, cx, cy, s=1.0):
    r = 14 * s
    c.setFillColor(C["orange"])
    p = c.beginPath()
    for i in range(5):
        a1 = math.radians(90 + i * 72)
        a2 = math.radians(90 + i * 72 + 36)
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        x2, y2 = cx + r * 0.45 * math.cos(a2), cy + r * 0.45 * math.sin(a2)
        if i == 0:
            p.moveTo(x1, y1)
        else:
            p.lineTo(x1, y1)
        p.lineTo(x2, y2)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    c.setFillColor(C["dark"])
    c.circle(cx - 2 * s, cy + 2 * s, 1.5 * s, fill=1, stroke=0)
    c.circle(cx + 2 * s, cy + 2 * s, 1.5 * s, fill=1, stroke=0)


def draw_coral(c, cx, cy, s=1.0):
    c.setStrokeColor(C["pink"])
    c.setLineWidth(3 * s)
    c.setLineCap(1)
    c.line(cx, cy - 12 * s, cx, cy + 10 * s)
    c.line(cx, cy, cx - 8 * s, cy + 10 * s)
    c.line(cx, cy, cx + 8 * s, cy + 10 * s)
    c.line(cx - 4 * s, cy + 5 * s, cx - 10 * s, cy + 12 * s)
    c.line(cx + 4 * s, cy + 5 * s, cx + 10 * s, cy + 12 * s)
    c.setLineCap(0)


# Ocean theme color palette - cool blues and aquatic tones
ocean_colors = {
    "backgrounds": [
        HexColor("#E0F4FF"),  # Light sky blue
        HexColor("#D4F1F4"),  # Aqua mist
        HexColor("#E0FFFF"),  # Light cyan
        HexColor("#D6F4F4"),  # Seafoam
        HexColor("#CCF2F4"),  # Pale turquoise
    ],
    "banners": [
        C["blue"],        # Ocean blue
        C["teal"],        # Teal
        HexColor("#4DB8D8"),  # Deeper aqua
        HexColor("#5DADE2"),  # Sky blue
        HexColor("#48C9B0"),  # Turquoise
    ],
    "accents": [
        C["blue"],
        C["teal"],
        HexColor("#3498DB"),  # Bright blue
        HexColor("#1ABC9C"),  # Turquoise
        C["purple"],
        HexColor("#5DADE2"),  # Light blue
    ]
}

register_theme(
    "ocean",
    start_icons=[draw_fish, draw_whale, draw_turtle],
    end_icons=[draw_shell, draw_starfish, draw_coral],
    shape_icons=[draw_starfish, draw_shell, draw_fish, draw_whale, draw_turtle, draw_coral],
    corner_icons=[draw_starfish, draw_shell, draw_coral],
    colors=ocean_colors,
)
