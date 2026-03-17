"""Rectangle tracing activity."""

from .base import WIDTH, HEIGHT
from .shape_base import ShapeActivity


class Rectangles(ShapeActivity):
    """Rectangle tracing activity."""

    name = "rectangles"
    title = "Trace the Rectangles"
    instruction = "Follow the dotted lines to trace each rectangle!"

    def get_positions(self):
        """Return list of (cx, cy, width, height, orientation) tuples."""
        return [
            (150, HEIGHT - 225, 110, 65, "horizontal"),
            (WIDTH / 2, HEIGHT - 225, 65, 110, "vertical"),
            (WIDTH - 150, HEIGHT - 225, 110, 65, "horizontal"),
            (150, HEIGHT - 450, 120, 75, "horizontal"),
            (WIDTH / 2, HEIGHT - 450, 75, 120, "vertical"),
            (WIDTH - 150, HEIGHT - 450, 120, 75, "horizontal"),
        ]

    def draw_shape(self, canvas, position_data, idx, page_idx, theme, layout):
        """Draw a single rectangle."""
        cx, cy, w, h, orientation = position_data
        x1 = cx - w / 2
        y1 = cy - h / 2
        canvas.rect(x1, y1, w, h, fill=0, stroke=1)

    def get_center(self, position_data):
        """Extract center from position_data."""
        cx, cy, w, h, orientation = position_data
        return cx, cy

    def get_icon_scale(self, position_data):
        """Calculate icon scale from dimensions."""
        cx, cy, w, h, orientation = position_data
        return min(w, h) * 0.016
