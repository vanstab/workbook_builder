"""Base class for simple shape tracing activities."""

from abc import abstractmethod
from ..colors import get_accent
from .base import Activity, WIDTH, HEIGHT


class ShapeActivity(Activity):
    """Base class for shape tracing activities (circles, squares, rectangles, etc.).

    Subclasses must define:
    - name: str (activity identifier)
    - title: str (display title)
    - instruction: str (user instruction)
    - get_positions(): method returning list of position tuples
    - draw_shape(): method to draw a single shape
    - get_icon(): method to get icon for a shape (optional)
    """

    def draw_content(self, canvas, page_idx, theme, layout):
        """Draw shapes in a grid."""
        positions = self.get_positions()

        for i, position_data in enumerate(positions):
            # Set stroke style
            col = get_accent(page_idx, i, theme)
            canvas.setStrokeColor(col)
            canvas.setLineWidth(layout["thickness"] + 0.5)
            canvas.setDash(*layout["dash"])

            # Draw the shape (subclass defines how)
            self.draw_shape(canvas, position_data, i, page_idx, theme, layout)

            # Reset dash
            canvas.setDash()

            # Draw icon in center (if provided by subclass)
            icon_func = self.get_icon(i, theme)
            if icon_func:
                icon_scale = self.get_icon_scale(position_data)
                cx, cy = self.get_center(position_data)
                icon_func(canvas, cx, cy, icon_scale)

    @abstractmethod
    def get_positions(self):
        """Return list of position tuples for shapes.

        Returns:
            list of tuples with position data (format varies by shape)

        Example:
            [(cx, cy, radius), (cx, cy, radius), ...]  # for circles
            [(cx, cy, width, height), ...]  # for rectangles
        """
        pass

    @abstractmethod
    def draw_shape(self, canvas, position_data, idx, page_idx, theme, layout):
        """Draw a single shape.

        Args:
            canvas: reportlab Canvas
            position_data: tuple with position info (format defined by get_positions)
            idx: position index (for variety)
            page_idx: page index
            theme: theme dictionary
            layout: layout configuration
        """
        pass

    @abstractmethod
    def get_center(self, position_data):
        """Extract center (cx, cy) from position_data.

        Args:
            position_data: tuple with position info

        Returns:
            tuple: (cx, cy)
        """
        pass

    @abstractmethod
    def get_icon_scale(self, position_data):
        """Calculate icon scale from position_data.

        Args:
            position_data: tuple with position info

        Returns:
            float: scale factor for icon
        """
        pass

    def get_icon(self, idx, theme):
        """Get icon function for this shape position.

        Default implementation uses theme["shape_icons"] and cycles through them.
        Override to use a fixed icon or different selection logic.

        Args:
            idx: position index
            theme: theme dictionary

        Returns:
            function or None: icon drawing function
        """
        icons = theme.get("shape_icons", [])
        if icons:
            return icons[idx % len(icons)]
        return None
