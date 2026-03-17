"""Circle tracing activity."""

from .base import WIDTH, HEIGHT
from .shape_base import ShapeActivity


class Circles(ShapeActivity):
    """Circle tracing activity."""

    name = "circles"
    title = "Trace the Circles"
    instruction = "Follow the dotted lines to trace each circle!"

    def get_positions(self):
        """Return list of (cx, cy, radius) tuples."""
        return [
            (150, HEIGHT - 235, 60),
            (WIDTH / 2, HEIGHT - 235, 60),
            (WIDTH - 150, HEIGHT - 235, 60),
            (150, HEIGHT - 445, 70),
            (WIDTH / 2, HEIGHT - 445, 70),
            (WIDTH - 150, HEIGHT - 445, 70),
        ]

    def draw_shape(self, canvas, position_data, idx, page_idx, theme, layout):
        """Draw a single circle."""
        cx, cy, r = position_data
        canvas.circle(cx, cy, r, fill=0, stroke=1)

    def get_center(self, position_data):
        """Extract center from position_data."""
        cx, cy, r = position_data
        return cx, cy

    def get_icon_scale(self, position_data):
        """Calculate icon scale from radius."""
        cx, cy, r = position_data
        return r * 0.018
