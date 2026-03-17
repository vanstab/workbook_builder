"""Space theme icons: rocket, alien, UFO, planet, moon."""

from ..colors import C, BG, HexColor
from . import register_theme, draw_star


def draw_rocket(c, cx, cy, s=1.0):
    c.setFillColor(C["white"])
    c.setStrokeColor(C["dark"])
    c.setLineWidth(0.5)
    c.rect(cx - 6 * s, cy - 12 * s, 12 * s, 20 * s, fill=1, stroke=1)
    c.setFillColor(C["red"])
    p = c.beginPath()
    p.moveTo(cx, cy + 16 * s)
    p.lineTo(cx - 6 * s, cy + 8 * s)
    p.lineTo(cx + 6 * s, cy + 8 * s)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    c.setFillColor(C["blue"])
    c.circle(cx, cy + 1 * s, 4 * s, fill=1, stroke=0)
    c.setFillColor(C["red"])
    for side in [-1, 1]:
        p = c.beginPath()
        p.moveTo(cx + side * 6 * s, cy - 12 * s)
        p.lineTo(cx + side * 12 * s, cy - 16 * s)
        p.lineTo(cx + side * 6 * s, cy - 4 * s)
        p.close()
        c.drawPath(p, fill=1, stroke=0)
    c.setFillColor(C["orange"])
    p = c.beginPath()
    p.moveTo(cx - 4 * s, cy - 12 * s)
    p.lineTo(cx, cy - 20 * s)
    p.lineTo(cx + 4 * s, cy - 12 * s)
    p.close()
    c.drawPath(p, fill=1, stroke=0)


def draw_alien(c, cx, cy, s=1.0):
    c.setFillColor(C["green"])
    c.ellipse(cx - 10 * s, cy - 4 * s, cx + 10 * s, cy + 12 * s, fill=1, stroke=0)
    c.setFillColor(C["white"])
    c.ellipse(cx - 8 * s, cy + 2 * s, cx - 2 * s, cy + 8 * s, fill=1, stroke=0)
    c.ellipse(cx + 2 * s, cy + 2 * s, cx + 8 * s, cy + 8 * s, fill=1, stroke=0)
    c.setFillColor(C["dark"])
    c.circle(cx - 4 * s, cy + 5 * s, 2 * s, fill=1, stroke=0)
    c.circle(cx + 4 * s, cy + 5 * s, 2 * s, fill=1, stroke=0)
    c.setFillColor(C["green"])
    c.ellipse(cx - 6 * s, cy - 14 * s, cx + 6 * s, cy - 2 * s, fill=1, stroke=0)
    c.setStrokeColor(C["green"])
    c.setLineWidth(1.5 * s)
    c.line(cx - 5 * s, cy + 12 * s, cx - 8 * s, cy + 18 * s)
    c.line(cx + 5 * s, cy + 12 * s, cx + 8 * s, cy + 18 * s)
    c.setFillColor(C["yellow"])
    c.circle(cx - 8 * s, cy + 18 * s, 2 * s, fill=1, stroke=0)
    c.circle(cx + 8 * s, cy + 18 * s, 2 * s, fill=1, stroke=0)


def draw_ufo(c, cx, cy, s=1.0):
    c.setFillColor(HexColor("#ADD8E6"))
    c.ellipse(cx - 8 * s, cy, cx + 8 * s, cy + 12 * s, fill=1, stroke=0)
    c.setFillColor(C["gray"])
    c.ellipse(cx - 18 * s, cy - 3 * s, cx + 18 * s, cy + 5 * s, fill=1, stroke=0)
    for dx in [-10, -3, 4, 11]:
        c.setFillColor(C["yellow"])
        c.circle(cx + dx * s, cy + 1 * s, 2 * s, fill=1, stroke=0)


def draw_planet(c, cx, cy, s=1.0):
    c.setFillColor(C["orange"])
    c.circle(cx, cy, 12 * s, fill=1, stroke=0)
    c.setStrokeColor(C["yellow"])
    c.setLineWidth(2 * s)
    c.ellipse(cx - 18 * s, cy - 4 * s, cx + 18 * s, cy + 4 * s, fill=0, stroke=1)


def draw_moon(c, cx, cy, s=1.0):
    c.setFillColor(C["yellow"])
    c.circle(cx, cy, 12 * s, fill=1, stroke=0)
    c.setFillColor(BG["yellow"])
    c.circle(cx + 5 * s, cy + 2 * s, 10 * s, fill=1, stroke=0)
    c.setFillColor(HexColor("#EED98B"))
    c.circle(cx - 4 * s, cy + 3 * s, 2 * s, fill=1, stroke=0)
    c.circle(cx - 2 * s, cy - 5 * s, 1.5 * s, fill=1, stroke=0)


# Space theme color palette - deep purples, blues, and cosmic colors
space_colors = {
    "backgrounds": [
        HexColor("#E8E0FF"),  # Pale lavender
        HexColor("#E0E6FF"),  # Light periwinkle
        HexColor("#D8D0FF"),  # Soft purple
        HexColor("#E6F0FF"),  # Cosmic blue
        HexColor("#DDD5FF"),  # Misty purple
    ],
    "banners": [
        C["purple"],      # Deep purple
        HexColor("#8E44AD"),  # Royal purple
        HexColor("#5B5EFF"),  # Cosmic blue
        HexColor("#9B59B6"),  # Amethyst
        HexColor("#6C5CE7"),  # Bright purple
    ],
    "accents": [
        C["purple"],
        HexColor("#8E44AD"),  # Purple
        C["blue"],
        HexColor("#9B59B6"),  # Amethyst
        C["pink"],
        HexColor("#A29BFE"),  # Light purple
    ]
}

register_theme(
    "space",
    start_icons=[draw_rocket, draw_alien, draw_ufo],
    end_icons=[draw_star, draw_planet, draw_moon],
    shape_icons=[draw_star, draw_planet, draw_moon, draw_rocket, draw_alien, draw_ufo],
    corner_icons=[draw_star, draw_moon, draw_planet],
    colors=space_colors,
)
