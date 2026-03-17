"""Letter tracing activity - one page per letter."""

from reportlab.lib.colors import HexColor
from HersheyFonts import HersheyFonts
from ..colors import C, get_accent, get_banner
from .base import Activity, WIDTH, HEIGHT


class LetterTracing(Activity):
    """Letter tracing activity - displays one letter per page (uppercase or lowercase)."""

    # Size presets
    SIZE_PRESETS = {
        "small": 60,
        "medium": 90,
        "large": 120,
        "extra-large": 150,
    }

    def __init__(self, letter, size="medium"):
        """Initialize letter tracing activity.

        Args:
            letter: str - single letter A-Z or a-z
            size: str or int - size preset name or font size in points (default: "medium")
        """
        self.letter = str(letter)

        # Handle size parameter
        if isinstance(size, str) and size in self.SIZE_PRESETS:
            self.font_size = self.SIZE_PRESETS[size]
            self.size_name = size
        elif isinstance(size, (int, float)):
            self.font_size = int(size)
            self.size_name = "custom"
        else:
            self.font_size = self.SIZE_PRESETS["medium"]
            self.size_name = "medium"

        # Use the letter itself for display, but sanitize for filename
        letter_name = self.letter.upper() if self.letter.isupper() else f"lower_{self.letter.lower()}"
        self.name = f"letter_{letter_name}_{self.size_name}"
        self.title = f"Trace the Letter {self.letter}"
        if self.size_name != "medium":
            self.title += f" ({self.size_name.replace('-', ' ').title()})"
        self.instruction = f"Trace the dashed lines to practice writing {self.letter}!"

    def draw_content(self, canvas, page_idx, theme, layout):
        """Draw the letter tracing content."""
        char = self.letter

        # 1. Draw stroke guide (example letter)
        self._draw_stroke_guide(canvas, char, page_idx)

        # 2. Draw grid of dashed outline letters for tracing
        self._draw_tracing_grid(canvas, char, page_idx, theme, layout)

    def _draw_stroke_guide(self, canvas, char, page_idx):
        """Draw the example letter in top-left."""
        guide_x = 55
        guide_y = HEIGHT - 160
        guide_size = 48

        # Draw rounded box
        canvas.saveState()
        canvas.setStrokeColor(C["gray"])
        canvas.setLineWidth(1)
        canvas.roundRect(guide_x - 10, guide_y - 10, 60, 70, 8, fill=0, stroke=1)
        canvas.restoreState()

        # Draw solid letter
        canvas.saveState()
        banner_col = get_banner(page_idx)
        canvas.setFont("Helvetica-Bold", guide_size)
        canvas.setFillColor(banner_col)
        canvas.drawString(guide_x, guide_y, char)
        canvas.restoreState()

    def effective_rows(self, layout):
        """Override to reduce rows for larger font sizes."""
        base_rows = layout["rows"]

        # Reduce rows for larger fonts to prevent cutoff
        if self.font_size >= 150:  # extra-large
            return min(base_rows, 2)
        elif self.font_size >= 120:  # large
            return min(base_rows, 3)
        elif self.font_size >= 90:  # medium
            return min(base_rows, 3)
        else:  # small
            return base_rows

    def _draw_tracing_grid(self, canvas, char, page_idx, theme, layout):
        """Draw grid of dashed outline letters with guide lines."""
        rows = self.effective_rows(layout)
        trace_font_size = self.font_size

        # Dynamic columns based on font size - larger fonts get fewer columns for more space
        if trace_font_size >= 150:  # extra-large
            cols = 3
            base_margin = 120
        elif trace_font_size >= 120:  # large
            cols = 4
            base_margin = 100
        elif trace_font_size >= 90:  # medium
            cols = 4
            base_margin = 100
        else:  # small
            cols = 5
            base_margin = 100

        # Adjust layout based on font size to prevent overlap with guide box
        # Larger fonts need the grid to start lower and need more vertical space
        base_y_top = HEIGHT - 230
        # Add extra space for larger fonts, using small (60pt) as baseline
        size_offset = max(0, (trace_font_size - 60) * 1.2)
        y_top = base_y_top - size_offset

        col_spacing = (WIDTH - base_margin) / cols

        # Dynamic row spacing based on font size
        # Adjust multiplier based on font size - larger fonts need tighter spacing
        if trace_font_size >= 150:  # extra-large
            spacing_multiplier = 1.4
        elif trace_font_size >= 120:  # large
            spacing_multiplier = 1.5
        elif trace_font_size >= 90:  # medium
            spacing_multiplier = 1.6
        else:  # small
            spacing_multiplier = 1.8

        min_row_height = trace_font_size * spacing_multiplier
        bottom_margin = 120
        available_height = y_top - bottom_margin
        calculated_spacing = available_height / max(rows, 1)
        row_spacing = max(min_row_height, calculated_spacing)

        for r in range(rows):
            y = y_top - r * row_spacing

            # Draw baseline (solid, light gray)
            canvas.saveState()
            canvas.setStrokeColor(HexColor("#E8E8E8"))
            canvas.setLineWidth(0.5)
            canvas.line(50, y, WIDTH - 50, y)
            canvas.restoreState()

            # Draw midline (dashed, lighter gray)
            canvas.saveState()
            canvas.setStrokeColor(HexColor("#F0F0F0"))
            canvas.setLineWidth(0.3)
            canvas.setDash(2, 4)
            canvas.line(50, y + trace_font_size * 0.35, WIDTH - 50, y + trace_font_size * 0.35)
            canvas.restoreState()

            # Draw letters in this row
            for col_idx in range(cols):
                x = 55 + col_idx * col_spacing
                trace_color = get_accent(page_idx, r + col_idx, theme)

                # Draw dashed outline letter for tracing
                self._draw_dotted_char(canvas, x, y, char, trace_font_size, trace_color)

    def _draw_dotted_char(self, canvas, x, y, char, size, color):
        """Draw a character with dashed single-stroke lines using Hershey fonts."""
        # Initialize Hershey font
        hf = HersheyFonts()
        hf.load_default_font()
        hf.normalize_rendering(size)

        # Get line segments for the character
        lines = list(hf.lines_for_text(char))

        if not lines:
            return

        # Calculate bounding box to center the character
        all_x = [coord for line in lines for point in line for coord in [point[0]]]
        all_y = [coord for line in lines for point in line for coord in [point[1]]]

        if not all_x or not all_y:
            return

        min_x, max_x = min(all_x), max(all_x)
        min_y, max_y = min(all_y), max(all_y)

        # Center offset
        width = max_x - min_x
        height = max_y - min_y
        offset_x = x - min_x
        offset_y = y - min_y

        # Draw each line segment with dashed stroke
        canvas.saveState()
        canvas.setStrokeColor(color)
        canvas.setLineWidth(2)
        canvas.setDash(4, 3)

        for (x1, y1), (x2, y2) in lines:
            canvas.line(offset_x + x1, offset_y + y1, offset_x + x2, offset_y + y2)

        canvas.restoreState()
