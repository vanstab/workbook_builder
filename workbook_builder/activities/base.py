"""Abstract base class that all activity renderers must implement."""

from abc import ABC, abstractmethod
from reportlab.lib.pagesizes import letter
from ..page import draw_page_bg, draw_banner, draw_subtitle, draw_footer, draw_corner_deco, draw_bottom_deco

WIDTH, HEIGHT = letter


class Activity(ABC):
    """Base class for a single worksheet activity page.

    Subclasses must define:
        name        – CLI identifier (e.g. "straight")
        title       – display title on the page banner
        instruction – subtitle text explaining the task

    Subclasses must implement:
        draw_content(canvas, page_idx, theme, layout)
    """

    name: str = ""
    title: str = ""
    instruction: str = ""

    # ── Public API ────────────────────────────────────────────────────

    def render(self, canvas, page_idx, total_pages, theme, layout):
        """Render one full page: background, banner, content, footer."""
        draw_page_bg(canvas, page_idx, theme)
        draw_banner(canvas, self.title, page_idx, theme)
        draw_subtitle(canvas, self.instruction)
        draw_corner_deco(canvas, theme, page_idx)
        self.draw_content(canvas, page_idx, theme, layout)
        draw_bottom_deco(canvas, theme, page_idx)
        draw_footer(canvas, page_idx, total_pages)

    # ── Subclass must implement ───────────────────────────────────────

    @abstractmethod
    def draw_content(self, canvas, page_idx, theme, layout):
        """Draw the main tracing content area of the page.

        Args:
            canvas:    reportlab Canvas
            page_idx:  0-based index of this page in the full worksheet
            theme:     dict with start_icons, end_icons, shape_icons, corner_icons
            layout:    dict with rows, thickness, dash
        """
        ...

    # ── Helpers available to all subclasses ────────────────────────────

    @staticmethod
    def content_top():
        """Y coordinate where the main content area begins."""
        return HEIGHT - 135

    @staticmethod
    def content_bottom():
        """Y coordinate above the footer decorations."""
        return 105

    def row_spacing(self, layout):
        """Vertical spacing between rows based on layout config."""
        rows = self.effective_rows(layout)
        return (self.content_top() - self.content_bottom()) / max(rows, 1)

    def effective_rows(self, layout):
        """Number of rows, clamped to what fits for this activity type."""
        return layout["rows"]

    @staticmethod
    def start_x():
        """X coordinate for left-side icons / line starts."""
        return 75

    @staticmethod
    def end_x():
        """X coordinate for right-side icons / line ends."""
        return 500

    @staticmethod
    def line_start():
        """X coordinate where the traceable line begins."""
        return 110

    @staticmethod
    def line_end():
        """X coordinate where the traceable line ends."""
        return 470
