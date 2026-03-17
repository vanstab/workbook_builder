"""Base class for math worksheet activities (addition, subtraction, etc.)."""

from abc import abstractmethod
from ..colors import get_accent
from .base import Activity, WIDTH, HEIGHT


class MathActivity(Activity):
    """Base class for math activities with problem grids.

    Subclasses must define:
    - operation_symbol: str (e.g., "+", "-", "×", "÷")
    - operation_name: str (e.g., "Addition", "Subtraction")
    - _generate_problems(): method to create problem sets
    """

    operation_symbol = "?"  # Override in subclasses
    operation_name = "Math"  # Override in subclasses

    def __init__(self, min_num=None, max_num=None, problems_per_page=None):
        """Initialize math activity.

        Args:
            min_num: Minimum number (0-100, default 0)
            max_num: Maximum number (0-100, default 10)
            problems_per_page: Number of problems per page (optional)
        """
        # Validate and store range
        self._min_num = max(0, min_num) if min_num is not None else 0
        self._max_num = min(100, max_num) if max_num is not None else 10
        self._custom_problems = problems_per_page

        # Ensure min <= max
        if self._min_num > self._max_num:
            self._min_num, self._max_num = self._max_num, self._min_num

        # Set name and title based on range
        if min_num is not None or max_num is not None:
            self.name = f"{self.operation_name.lower()}_{self._min_num}_{self._max_num}"
            self.title = f"{self.operation_name} Practice ({self._min_num}-{self._max_num})"
        else:
            self.name = self.operation_name.lower()
            self.title = f"{self.operation_name} Practice"

        self.instruction = f"Solve each {self.operation_name.lower()} problem and write the answer in the box!"

    def draw_content(self, canvas, page_idx, theme, layout):
        """Draw math problems in a grid layout."""
        # Use custom settings if provided, otherwise fall back to layout
        min_num = self._min_num if hasattr(self, '_min_num') else layout.get("min_num", 0)
        max_num = self._max_num if hasattr(self, '_max_num') else layout.get("max_num", 10)
        problems_per_page = self._custom_problems or layout.get("problems_per_page", 12)

        # Generate problems deterministically
        problems = self._generate_problems(page_idx, min_num, max_num, problems_per_page)

        # Draw grid of problems
        self._draw_problem_grid(canvas, problems, page_idx, theme)

    @abstractmethod
    def _generate_problems(self, page_idx, min_num, max_num, count):
        """Generate unique problems deterministically.

        Args:
            page_idx: Page index for seeding
            min_num: Minimum number (0-100)
            max_num: Maximum number (0-100)
            count: Number of problems to generate

        Returns:
            list of (a, b, answer) tuples with no duplicates
        """
        pass

    def _draw_problem_grid(self, canvas, problems, page_idx, theme):
        """Draw problems in 2-column grid.

        Args:
            canvas: reportlab Canvas
            problems: list of (a, b, answer) tuples
            page_idx: Page index for color selection
            theme: Theme dictionary with icon sets
        """
        cols = 2
        rows = (len(problems) + 1) // 2

        # Layout dimensions
        top_y = self.content_top() - 30
        bottom_y = self.content_bottom() + 20
        available_height = top_y - bottom_y
        row_height = available_height / max(rows, 1)

        col_width = (WIDTH - 120) / cols
        left_col_x = 80

        # Draw each problem
        icons = theme["shape_icons"]

        for idx, (a, b, answer) in enumerate(problems):
            col = idx % cols
            row = idx // cols

            # Position
            x = left_col_x + col * col_width + col_width / 2
            y = top_y - row * row_height - row_height / 2

            # Draw problem
            color = get_accent(page_idx, idx, theme)
            self._draw_single_problem(canvas, x, y, a, b, color)

            # Optional: Add small themed icon near some problems
            if idx % 4 == (page_idx % 4):  # Deterministic decoration
                icon = icons[idx % len(icons)]
                icon_x = x + 95
                icon_y = y - 5
                icon(canvas, icon_x, icon_y, 0.4)

    def _draw_single_problem(self, canvas, cx, cy, a, b, color):
        """Draw a single horizontal math problem: a ⊙ b = __

        Args:
            canvas: reportlab Canvas
            cx, cy: center position of problem
            a, b: numbers to operate on
            color: accent color for this problem
        """
        problem_font_size = 28

        # Draw: a ⊙ b = __
        canvas.saveState()
        canvas.setFont("Helvetica-Bold", problem_font_size)
        canvas.setFillColor(color)

        # Calculate widths for centering
        # Format: "a  ⊙  b  =  "
        problem_text = f"{a}  {self.operation_symbol}  {b}  ="
        problem_width = canvas.stringWidth(problem_text, "Helvetica-Bold", problem_font_size)

        # Draw problem text
        text_x = cx - problem_width / 2 - 30  # -30 for answer box space
        canvas.drawString(text_x, cy, problem_text)

        # Draw answer box (rounded rectangle)
        box_x = text_x + problem_width + 10
        box_y = cy - 5
        box_width = 50
        box_height = 40

        canvas.setStrokeColor(color)
        canvas.setLineWidth(2)
        canvas.roundRect(box_x, box_y, box_width, box_height, 6, fill=0, stroke=1)

        canvas.restoreState()
