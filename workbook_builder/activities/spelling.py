"""Spelling activity - trace simple words."""

import os
from reportlab.lib.colors import HexColor
from HersheyFonts import HersheyFonts
from ..colors import C, get_accent, get_banner
from .base import Activity, WIDTH, HEIGHT


def load_words():
    """Load words from words.txt file."""
    words_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "words.txt")
    try:
        with open(words_file, 'r') as f:
            words = [line.strip() for line in f if line.strip()]
        return words
    except FileNotFoundError:
        # Fallback words if file not found
        return ["cat", "dog", "sun", "bee", "car", "hat", "bug", "pig", "fox", "bat"]


class Spelling(Activity):
    """Spelling activity - displays simple words to trace."""

    def __init__(self, min_length=None, max_length=None):
        """Initialize spelling activity.

        Args:
            min_length: Minimum word length (default: None = no minimum)
            max_length: Maximum word length (default: None = no maximum)
        """
        self.min_length = min_length
        self.max_length = max_length

        # Load and filter words
        all_words = load_words()
        self.words = self._filter_words(all_words)

        # Set activity metadata
        self.name = "spelling"
        self.title = "Trace the Words"
        if min_length and max_length:
            self.title = f"Trace {min_length}-{max_length} Letter Words"
        elif min_length:
            self.title = f"Trace {min_length}+ Letter Words"
        elif max_length:
            self.title = f"Trace Short Words ({max_length} letters max)"
        self.instruction = "Follow the dashed lines to practice spelling!"

    def _filter_words(self, words):
        """Filter words based on min/max length."""
        filtered = words

        if self.min_length is not None:
            filtered = [w for w in filtered if len(w) >= self.min_length]

        if self.max_length is not None:
            filtered = [w for w in filtered if len(w) <= self.max_length]

        # If no words match, use all words
        if not filtered:
            return words

        return filtered

    def draw_content(self, canvas, page_idx, theme, layout):
        """Draw the word tracing content."""
        # Select 3 words for this page based on page_idx
        words_per_page = 3
        start_idx = (page_idx * words_per_page) % len(self.words)
        page_words = [self.words[(start_idx + i) % len(self.words)] for i in range(words_per_page)]

        # Draw word tracing rows
        self._draw_word_rows(canvas, page_words, page_idx, theme, layout)

    def _draw_word_rows(self, canvas, words, page_idx, theme, layout):
        """Draw rows of words to trace."""
        y_start = HEIGHT - 220
        row_spacing = 180
        font_size = 60

        for row_idx, word in enumerate(words):
            y = y_start - row_idx * row_spacing

            # 1. Draw example word in a box (left side)
            self._draw_example_word(canvas, word, 70, y, page_idx)

            # 2. Draw baseline
            baseline_y = y - 20
            canvas.saveState()
            canvas.setStrokeColor(HexColor("#E8E8E8"))
            canvas.setLineWidth(0.5)
            canvas.line(180, baseline_y, WIDTH - 50, baseline_y)
            canvas.restoreState()

            # 3. Draw midline (dashed)
            canvas.saveState()
            canvas.setStrokeColor(HexColor("#F0F0F0"))
            canvas.setLineWidth(0.3)
            canvas.setDash(2, 4)
            canvas.line(180, baseline_y + font_size * 0.35, WIDTH - 50, baseline_y + font_size * 0.35)
            canvas.restoreState()

            # 4. Draw traced word once
            trace_color = get_accent(page_idx, row_idx, theme)

            # Center the traced word in available space
            x = 240
            self._draw_traced_word(canvas, word, x, baseline_y, font_size, trace_color)

    def _draw_example_word(self, canvas, word, x, y, page_idx):
        """Draw solid example word in a rounded box."""
        # Calculate box size based on word length
        box_width = max(80, len(word) * 18)
        box_height = 70

        # Draw rounded box
        canvas.saveState()
        canvas.setStrokeColor(C["gray"])
        canvas.setLineWidth(1)
        canvas.roundRect(x - 10, y - 35, box_width, box_height, 8, fill=0, stroke=1)
        canvas.restoreState()

        # Draw solid word
        canvas.saveState()
        banner_col = get_banner(page_idx)
        canvas.setFont("Helvetica-Bold", 28)
        canvas.setFillColor(banner_col)
        canvas.drawString(x, y, word)
        canvas.restoreState()

    def _draw_traced_word(self, canvas, word, x, y, size, color):
        """Draw a word with dashed single-stroke lines using Hershey fonts."""
        # Initialize Hershey font
        hf = HersheyFonts()
        hf.load_default_font()
        hf.normalize_rendering(size)

        # Get line segments for the word
        lines = list(hf.lines_for_text(word))

        if not lines:
            return

        # Calculate bounding box
        all_x = [coord for line in lines for point in line for coord in [point[0]]]
        all_y = [coord for line in lines for point in line for coord in [point[1]]]

        if not all_x or not all_y:
            return

        min_x, max_x = min(all_x), max(all_x)
        min_y, max_y = min(all_y), max(all_y)

        # Offset
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
