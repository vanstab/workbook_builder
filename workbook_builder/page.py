"""Page-level drawing utilities: backgrounds, banners, footers, decorations."""

from reportlab.lib.pagesizes import letter
from .colors import C, get_bg, get_banner, get_encouragement

WIDTH, HEIGHT = letter


def draw_page_bg(canvas, page_idx, theme=None):
    """Fill the page with a rotating pastel background."""
    canvas.setFillColor(get_bg(page_idx, theme))
    canvas.rect(0, 0, WIDTH, HEIGHT, fill=1, stroke=0)


def draw_banner(canvas, title, page_idx, theme=None):
    """Draw the colored title banner at the top of the page."""
    color = get_banner(page_idx, theme)
    canvas.setFillColor(color)
    canvas.roundRect(40, HEIGHT - 80, WIDTH - 80, 55, 18, fill=1, stroke=0)
    canvas.setFillColor(C["white"])
    canvas.setFont("Helvetica-Bold", 26)
    canvas.drawCentredString(WIDTH / 2, HEIGHT - 62, title)


def draw_subtitle(canvas, text):
    """Draw the instruction subtitle below the banner."""
    canvas.setFillColor(C["dark"])
    canvas.setFont("Helvetica", 13)
    canvas.drawCentredString(WIDTH / 2, HEIGHT - 100, text)


def draw_footer(canvas, page_idx, total_pages):
    """Draw encouragement message and page number at the bottom."""
    canvas.setFillColor(C["dark"])
    canvas.setFont("Helvetica-BoldOblique", 11)
    canvas.drawCentredString(WIDTH / 2, 45, get_encouragement(page_idx))
    canvas.setFillColor(C["gray"])
    canvas.setFont("Helvetica", 9)
    canvas.drawCentredString(WIDTH / 2, 18, f"Page {page_idx + 1} of {total_pages}")


def draw_corner_deco(canvas, theme, page_idx):
    """Draw small themed icons in the top corners of the banner."""
    icons = theme["corner_icons"]
    icon = icons[page_idx % len(icons)]
    icon(canvas, 60, HEIGHT - 52, 0.7)
    icon(canvas, WIDTH - 60, HEIGHT - 52, 0.7)


def draw_bottom_deco(canvas, theme, page_idx):
    """Draw a row of small themed icons above the footer."""
    icons = theme["shape_icons"]
    for i in range(6):
        icon = icons[(page_idx + i) % len(icons)]
        icon(canvas, 80 + i * 80, 80, 0.5)
