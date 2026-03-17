"""Square tracing activity."""

from ..icons import draw_star
from .base import WIDTH, HEIGHT
from .shape_base import ShapeActivity


class Squares(ShapeActivity):
    """Square tracing activity."""

    name = "squares"
    title = "Trace the Squares"
    instruction = "Follow the dotted lines to trace each square!"

    def get_positions(self):
        """Return list of (cx, cy, size) tuples."""
        return [
            (150, HEIGHT - 225, 85),
            (WIDTH / 2, HEIGHT - 225, 85),
            (WIDTH - 150, HEIGHT - 225, 85),
            (150, HEIGHT - 450, 100),
            (WIDTH / 2, HEIGHT - 450, 100),
            (WIDTH - 150, HEIGHT - 450, 100),
        ]

    def draw_shape(self, canvas, position_data, idx, page_idx, theme, layout):
        """Draw a single square."""
        cx, cy, sz = position_data
        canvas.rect(cx - sz / 2, cy - sz / 2, sz, sz, fill=0, stroke=1)

    def get_center(self, position_data):
        """Extract center from position_data."""
        cx, cy, sz = position_data
        return cx, cy

    def get_icon_scale(self, position_data):
        """Calculate icon scale from size."""
        cx, cy, sz = position_data
        return sz * 0.016

    def get_icon(self, idx, theme):
        """Use fixed star icon for all squares."""
        return draw_star
