"""Shared icon drawing functions and theme registry.

Every icon follows the signature: draw_xxx(canvas, cx, cy, scale=1.0)
"""

import math
from ..colors import C, BG, HexColor

# ── Shared icons (used by multiple themes) ────────────────────────────

def draw_star(c, cx, cy, s=1.0):
    r = 14 * s
    c.setFillColor(C["yellow"])
    c.setStrokeColor(C["yellow"])
    p = c.beginPath()
    for i in range(5):
        a1 = math.radians(90 + i * 72)
        a2 = math.radians(90 + i * 72 + 36)
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        x2, y2 = cx + r * 0.4 * math.cos(a2), cy + r * 0.4 * math.sin(a2)
        if i == 0:
            p.moveTo(x1, y1)
        else:
            p.lineTo(x1, y1)
        p.lineTo(x2, y2)
    p.close()
    c.drawPath(p, fill=1)


def draw_heart(c, cx, cy, s=1.0):
    sz = 10 * s
    c.setFillColor(C["pink"])
    p = c.beginPath()
    for i in range(51):
        t = 2 * math.pi * i / 50
        x = 16 * math.sin(t) ** 3
        y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        px, py = cx + x * sz / 18, cy + y * sz / 18
        if i == 0:
            p.moveTo(px, py)
        else:
            p.lineTo(px, py)
    p.close()
    c.drawPath(p, fill=1, stroke=0)


def draw_flower(c, cx, cy, s=1.0):
    sz = 16 * s
    c.setFillColor(C["pink"])
    for angle in range(0, 360, 60):
        rad = math.radians(angle)
        px = cx + sz * 0.6 * math.cos(rad)
        py = cy + sz * 0.6 * math.sin(rad)
        c.circle(px, py, sz * 0.4, fill=1, stroke=0)
    c.setFillColor(C["yellow"])
    c.circle(cx, cy, sz * 0.3, fill=1, stroke=0)


def draw_smiley(c, cx, cy, s=1.0):
    r = 14 * s
    c.setFillColor(HexColor("#FFF3C4"))
    c.circle(cx, cy, r, fill=1, stroke=0)
    c.setFillColor(C["white"])
    c.circle(cx - r * 0.3, cy + r * 0.2, r * 0.18, fill=1, stroke=0)
    c.circle(cx + r * 0.3, cy + r * 0.2, r * 0.18, fill=1, stroke=0)
    c.setFillColor(C["dark"])
    c.circle(cx - r * 0.3, cy + r * 0.2, r * 0.09, fill=1, stroke=0)
    c.circle(cx + r * 0.3, cy + r * 0.2, r * 0.09, fill=1, stroke=0)
    c.setStrokeColor(C["dark"])
    c.setLineWidth(1.5 * s)
    p = c.beginPath()
    for i in range(0, 181, 10):
        rad = math.radians(i + 180)
        x = cx + r * 0.4 * math.cos(rad)
        y = cy - r * 0.15 + r * 0.25 * math.sin(rad)
        if i == 0:
            p.moveTo(x, y)
        else:
            p.lineTo(x, y)
    c.drawPath(p, fill=0)


# ── Theme registry (populated by theme modules) ──────────────────────

THEMES = {}


def register_theme(name, start_icons, end_icons, shape_icons, corner_icons, colors=None):
    """Register a theme with its icon sets and color palette."""
    THEMES[name] = {
        "start_icons": start_icons,
        "end_icons": end_icons,
        "shape_icons": shape_icons,
        "corner_icons": corner_icons,
        "colors": colors or {},  # Optional theme-specific colors
    }


def get_theme(name):
    """Retrieve a registered theme by name."""
    return THEMES[name]


def available_themes():
    """Return list of registered theme names."""
    return list(THEMES.keys())


# ── Import all theme modules to trigger registration ──────────────────
from . import animals, ocean, space, garden, food  # noqa: E402, F401
