"""Oval tracing activity."""

from ..icons import draw_smiley
from .base import WIDTH, HEIGHT
from .shape_base import ShapeActivity


class Ovals(ShapeActivity):
    """Oval tracing activity."""

    name = "ovals"
    title = "Trace the Ovals"
    instruction = "Follow the dotted lines to trace each oval!"

    def get_positions(self):
        """Return list of (cx, cy, width, height, orientation) tuples."""
        return [
            (150, HEIGHT - 235, 80, 55, "horizontal"),
            (WIDTH / 2, HEIGHT - 235, 55, 80, "vertical"),
            (WIDTH - 150, HEIGHT - 235, 80, 55, "horizontal"),
            (150, HEIGHT - 445, 90, 65, "horizontal"),
            (WIDTH / 2, HEIGHT - 445, 65, 90, "vertical"),
            (WIDTH - 150, HEIGHT - 445, 90, 65, "horizontal"),
        ]

    def draw_shape(self, canvas, position_data, idx, page_idx, theme, layout):
        """Draw a single oval (ellipse)."""
        cx, cy, w, h, orientation = position_data
        x1 = cx - w / 2
        y1 = cy - h / 2
        x2 = cx + w / 2
        y2 = cy + h / 2
        canvas.ellipse(x1, y1, x2, y2, fill=0, stroke=1)

    def get_center(self, position_data):
        """Extract center from position_data."""
        cx, cy, w, h, orientation = position_data
        return cx, cy

    def get_icon_scale(self, position_data):
        """Calculate icon scale from dimensions."""
        cx, cy, w, h, orientation = position_data
        return min(w, h) * 0.016

    def get_icon(self, idx, theme):
        """Use fixed smiley icon for all ovals."""
        return draw_smiley
