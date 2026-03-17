"""Diamond tracing activity (gemstone/kite shape)."""

from ..icons import draw_flower
from .base import WIDTH, HEIGHT
from .shape_base import ShapeActivity


class Diamonds(ShapeActivity):
    """Diamond tracing activity."""

    name = "diamonds"
    title = "Trace the Diamonds"
    instruction = "Follow the dotted lines to trace each diamond!"

    def get_positions(self):
        """Return list of (cx, cy, width, height) tuples."""
        return [
            (150, HEIGHT - 235, 60, 50),
            (WIDTH / 2, HEIGHT - 235, 60, 50),
            (WIDTH - 150, HEIGHT - 235, 60, 50),
            (150, HEIGHT - 445, 70, 60),
            (WIDTH / 2, HEIGHT - 445, 70, 60),
            (WIDTH - 150, HEIGHT - 445, 70, 60),
        ]

    def draw_shape(self, canvas, position_data, idx, page_idx, theme, layout):
        """Draw a single diamond (kite/gemstone shape)."""
        cx, cy, w, h = position_data

        # Diamond points: top, right, bottom, left
        points = [
            (cx, cy + h),      # top
            (cx + w, cy),      # right
            (cx, cy - h),      # bottom
            (cx - w, cy),      # left
        ]

        p = canvas.beginPath()
        p.moveTo(points[0][0], points[0][1])
        for x, y in points[1:]:
            p.lineTo(x, y)
        p.close()
        canvas.drawPath(p, fill=0, stroke=1)

    def get_center(self, position_data):
        """Extract center from position_data."""
        cx, cy, w, h = position_data
        return cx, cy

    def get_icon_scale(self, position_data):
        """Calculate icon scale from dimensions."""
        cx, cy, w, h = position_data
        return min(w, h) * 0.018

    def get_icon(self, idx, theme):
        """Use fixed flower icon for all diamonds."""
        return draw_flower
