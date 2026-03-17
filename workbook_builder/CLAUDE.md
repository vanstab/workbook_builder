# CLAUDE.md — Workbook Generator

## Project Overview

A CLI-based Python tool that generates customizable workbook / tracing worksheet PDFs for young children (ages 2-5). Uses `reportlab` for PDF generation.

```bash
# Example usage
python -m workbook_builder --activities straight wavy zigzag --theme animals
python -m workbook_builder --activities numbers --numbers 1 2 3 --theme space
python -m workbook_builder --activities all --theme garden --rows 4
python -m workbook_builder --activities straight numbers letters --numbers all --letters A B C
```

## Architecture

```
workbook_builder/
├── __init__.py              ✅ Done - package init with __version__
├── __main__.py              ❌ TODO - CLI entry point (argparse)
├── colors.py                ✅ Done - color constants, palettes, dash styles, rotation helpers
├── page.py                  ✅ Done - page-level drawing (bg, banner, subtitle, footer, corner/bottom decorations)
├── icons/
│   ├── __init__.py          ✅ Done - shared icons (star, heart, flower, smiley) + theme registry + imports all themes
│   ├── animals.py           ✅ Done - bee, caterpillar, fish, butterfly
│   ├── ocean.py             ✅ Done - whale, turtle, shell, starfish, coral
│   ├── space.py             ✅ Done - rocket, alien, UFO, planet, moon
│   ├── garden.py            ✅ Done - ladybug, snail, worm, mushroom, leaf
│   └── food.py              ✅ Done - apple, cherry, cupcake, ice cream, cookie, lollipop
├── activities/
│   ├── __init__.py          ❌ TODO - activity registry (imports all activities, exposes ACTIVITY_REGISTRY dict + ALL_ACTIVITIES list)
│   ├── base.py              ✅ Done - abstract base class (Activity)
│   ├── straight.py          ✅ Done - StraightLines
│   ├── wavy.py              ✅ Done - WavyLines
│   ├── zigzag.py            ✅ Done - ZigzagLines
│   ├── diagonals.py         ✅ Done - DiagonalLines
│   ├── waves.py             ✅ Done - Waves (sine wave patterns)
│   ├── loops.py             ✅ Done - Loops (cursive writing loops)
│   ├── circles.py           ✅ Done - Circles
│   ├── squares.py           ✅ Done - Squares
│   ├── triangles.py         ✅ Done - Triangles
│   ├── spirals.py           ✅ Done - Spirals
│   ├── numbers.py           ❌ TODO - NumberTracing (one page per number)
│   └── letters.py           ❌ TODO - LetterTracing (one page per letter)
└── generator.py             ❌ TODO - orchestrator (builds page list from args, creates PDF)
```

## What's Done

### colors.py
- `C` dict: core colors (pink, orange, blue, green, purple, yellow, red, teal, gray, dark, white, light_green)
- `BG` dict: pastel page backgrounds (cream, blue, pink, green, purple, orange, yellow)
- Rotating lists: `ACCENT_COLORS`, `BG_LIST`, `BANNER_COLORS`, `ENCOURAGEMENTS`
- Helpers: `get_accent(page_idx, row)`, `get_bg(page_idx)`, `get_banner(page_idx)`, `get_encouragement(page_idx)`
- `parse_dash_style(style)` → returns `(dash, gap)` tuple for reportlab

### page.py
- `draw_page_bg(canvas, page_idx)` — fills full page with rotating pastel
- `draw_banner(canvas, title, page_idx)` — colored rounded rect banner at top
- `draw_subtitle(canvas, text)` — instruction text below banner
- `draw_footer(canvas, page_idx, total_pages)` — encouragement + page number
- `draw_corner_deco(canvas, theme, page_idx)` — small themed icons in banner corners
- `draw_bottom_deco(canvas, theme, page_idx)` — row of 6 small icons above footer

### icons/__init__.py
- Shared icons: `draw_star`, `draw_heart`, `draw_flower`, `draw_smiley`
- Theme registry: `register_theme(name, start_icons, end_icons, shape_icons, corner_icons)`
- `get_theme(name)`, `available_themes()`, `THEMES` dict
- Auto-imports all 5 theme modules at bottom

### Icon signature convention
Every icon function follows: `def draw_xxx(canvas, cx, cy, s=1.0)` where `s` is a uniform scale factor (default 1.0 = ~28px wide).

### Theme structure
Each theme provides:
```python
{
    "start_icons": [func, func, func],      # 3 icons for left side of line-tracing rows
    "end_icons": [func, func, func],         # 3 icons for right side
    "shape_icons": [func, ...],              # 6 icons for shape interiors & bottom deco
    "corner_icons": [func, func, func],      # 3 icons for banner corners
}
```

### Activity base class (activities/base.py)
```python
class Activity(ABC):
    name: str           # CLI identifier e.g. "straight"
    title: str          # Banner title e.g. "Straight Lines"
    instruction: str    # Subtitle e.g. "Trace the dotted lines..."

    def render(self, canvas, page_idx, total_pages, theme, layout):
        # Draws full page: bg → banner → subtitle → corners → draw_content → bottom_deco → footer

    @abstractmethod
    def draw_content(self, canvas, page_idx, theme, layout):
        # Subclass implements this - draws the main tracing content

    # Helpers:
    content_top() → HEIGHT - 135      # Y where content starts
    content_bottom() → 105            # Y above footer deco
    row_spacing(layout) → float       # vertical spacing between rows
    effective_rows(layout) → int      # rows, can be overridden to cap
    start_x() → 75                    # left icon X
    end_x() → 500                     # right icon X
    line_start() → 110                # traceable line start X
    line_end() → 470                  # traceable line end X
```

### Layout dict passed to activities
```python
layout = {
    "rows": int,           # 3-6, from --rows
    "thickness": float,    # 2.0-5.0, from --line-thickness
    "dash": (dash, gap),   # from --guide-style: dashed=(8,6), dotted=(3,4), solid=([],0)
}
```

## What's TODO

### 1. `activities/__init__.py` — Activity Registry
Should import all activity classes and build:
```python
ACTIVITY_REGISTRY = {
    "straight": StraightLines(),
    "wavy": WavyLines(),
    ...
}
ALL_ACTIVITIES = list(ACTIVITY_REGISTRY.keys())  # excludes "numbers" and "letters"
```
Numbers and letters are special — they generate multiple pages (one per number/letter), so they need separate handling in the generator.

### 2. `activities/numbers.py` — Number Tracing
One page per number. Each page has:
- Banner: "Trace the Number 3"
- Stroke guide: small solid number in a rounded box (top-left) with a green "start" dot
- Tracing area: grid of `rows × 5` large dotted-outline numbers to trace
- Baseline + midline guide rules for each row
- Themed decorations

Key technique for dotted character outlines:
```python
canvas.setFont("Helvetica-Bold", size)
canvas.setStrokeColor(color)
canvas.setLineWidth(2)
canvas.setDash(4, 3)
canvas._code.append("1 Tr")   # PDF text render mode: stroke only
canvas.drawString(x, y, char)
canvas._code.append("0 Tr")   # reset to fill mode
```

Should subclass `Activity` but override `render()` since it needs the number argument, or be a factory that returns configured Activity instances per number. A reasonable approach:

```python
class NumberTracing(Activity):
    def __init__(self, number):
        self.number = number
        self.name = f"number_{number}"
        self.title = f"Trace the Number {number}"
        self.instruction = f"Follow the dots to write the number {number}!"
```

### 3. `activities/letters.py` — Letter Tracing
Same structure as numbers but for uppercase letters A-Z. Identical layout approach.

### 4. `generator.py` — Orchestrator
Builds the ordered page list from CLI args and creates the PDF:
```python
def build_page_list(args) -> list[tuple]:
    """Returns list of (Activity_instance, extra_arg_or_None)."""
    # "all" expands to ALL_ACTIVITIES + numbers/letters if those flags are set
    # "numbers" expands to one NumberTracing per requested number
    # "letters" expands to one LetterTracing per requested letter

def generate(args):
    """Create the PDF."""
    pages = build_page_list(args)
    pdf = canvas.Canvas(output, pagesize=letter)
    for i, activity in enumerate(pages):
        if i > 0:
            pdf.showPage()
        activity.render(pdf, i, len(pages), theme, layout)
    pdf.save()
```

### 5. `__main__.py` — CLI Entry Point
argparse with these arguments:
```
--activities    nargs=+    default=["all"]     Activity types or "all"
--theme         str        default="animals"   One of: animals, ocean, space, garden, food
--numbers       nargs=*    default=None         0-9 or "all" (activates numbers if given)
--letters       nargs=*    default=None         A-Z or "all" (activates letters if given)
--rows          int        default=5            Rows per line-tracing page (3-6)
--line-thickness float     default=3.0          Guide line thickness (2-5)
--guide-style   str        default="dashed"     dashed | dotted | solid
--output / -o   str        default=auto         Output filename (default: worksheet_<theme>.pdf)
```

Edge cases to handle:
- `--numbers` with no values → default to "all" (0-9)
- `--letters` with no values → default to "all" (A-Z)
- If `--numbers`/`--letters` flags are given but not in `--activities`, auto-add them
- `--activities all` should expand to all 9 base activities + numbers if `--numbers` is set + letters if `--letters` is set

## Dependencies
- `reportlab` (PDF generation) — the only external dependency
- Python 3.10+

## Running Tests
From the project root:
```bash
# All activities, all themes
python -m workbook_builder --activities all --theme animals -o test_animals.pdf
python -m workbook_builder --activities all --theme ocean -o test_ocean.pdf
python -m workbook_builder --activities all --theme space -o test_space.pdf
python -m workbook_builder --activities all --theme garden -o test_garden.pdf
python -m workbook_builder --activities all --theme food -o test_food.pdf

# Numbers subset
python -m workbook_builder --activities numbers --numbers 1 2 3 --theme space -o test_nums.pdf

# Letters subset
python -m workbook_builder --activities letters --letters A B C --theme garden -o test_letters.pdf

# Mixed
python -m workbook_builder --activities straight wavy numbers --numbers 0 1 --theme food -o test_mix.pdf

# Layout options
python -m workbook_builder --activities straight --rows 3 --line-thickness 5 --guide-style dotted -o test_layout.pdf
```

## Prior Working Reference
The file `workbook_builder_reference.py` (single-file version) in this directory contains a fully working monolithic implementation. It can serve as reference for any behavior questions. The modular version should produce identical output.

## Design Notes
- Page size is US Letter (612 × 792 points)
- Each activity gets its own full page
- Colors and backgrounds rotate across pages for visual variety
- All icons scale via a single `s` parameter
- reportlab Canvas coordinate system: (0,0) is bottom-left, y increases upward
