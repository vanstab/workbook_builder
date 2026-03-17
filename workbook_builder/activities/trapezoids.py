"""Trapezoid tracing activity."""

from ..icons import draw_smiley
from .base import WIDTH, HEIGHT
from .shape_base import ShapeActivity


class Trapezoids(ShapeActivity):
    """Trapezoid tracing activity."""

    name = "trapezoids"
    title = "Trace the Trapezoids"
    instruction = "Follow the dotted lines to trace each trapezoid!"

    def get_positions(self):
        """Return list of (cx, cy, width) tuples."""
        return [
            (150, HEIGHT - 235, 90),
            (WIDTH / 2, HEIGHT - 235, 90),
            (WIDTH - 150, HEIGHT - 235, 90),
            (150, HEIGHT - 445, 105),
            (WIDTH / 2, HEIGHT - 445, 105),
            (WIDTH - 150, HEIGHT - 445, 105),
        ]

    def draw_shape(self, canvas, position_data, idx, page_idx, theme, layout):
        """Draw a single trapezoid (wider at bottom, narrower at top)."""
        cx, cy, width = position_data

        height = width * 0.7
        top_width = width * 0.6
        bottom_width = width

        # Trapezoid points: top-left, top-right, bottom-right, bottom-left
        points = [
            (cx - top_width / 2, cy + height / 2),      # top-left
            (cx + top_width / 2, cy + height / 2),      # top-right
            (cx + bottom_width / 2, cy - height / 2),   # bottom-right
            (cx - bottom_width / 2, cy - height / 2),   # bottom-left
        ]

        p = canvas.beginPath()
        p.moveTo(points[0][0], points[0][1])
        for x, y in points[1:]:
            p.lineTo(x, y)
        p.close()
        canvas.drawPath(p, fill=0, stroke=1)

    def get_center(self, position_data):
        """Extract center from position_data."""
        cx, cy, width = position_data
        return cx, cy

    def get_icon_scale(self, position_data):
        """Calculate icon scale from width."""
        cx, cy, width = position_data
        return width * 0.016

    def get_icon(self, idx, theme):
        """Use fixed smiley icon for all trapezoids."""
        return draw_smiley
