"""CLI entry point for Workbook Generator."""

import argparse
import sys
from .generator import generate
from .icons import available_themes
from .validators import parse_numeric_range


def parse_number_arg(value):
    """Parse a number argument - can be 0-9 or 'all'."""
    if value == "all":
        return list(range(10))
    try:
        num = int(value)
        if 0 <= num <= 9:
            return num
        else:
            raise ValueError(f"Number must be 0-9, got {num}")
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid number: {value}")


def parse_letter_arg(value):
    """Parse a letter argument - can be A-Z, a-z, or 'all'/'ALL'."""
    if value.lower() == "all":
        return [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    if value.lower() == "all-lower":
        return [chr(i) for i in range(ord('a'), ord('z') + 1)]
    if value.lower() == "all-both":
        return [chr(i) for i in range(ord('A'), ord('Z') + 1)] + [chr(i) for i in range(ord('a'), ord('z') + 1)]
    # Preserve case - don't force uppercase
    if len(value) == 1 and value.isalpha():
        return value
    else:
        raise argparse.ArgumentTypeError(f"Invalid letter: {value} (must be A-Z or a-z)")


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Generate customizable workbook worksheet PDFs for young children.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Custom page order (recommended!)
  python -m workbook_builder --pages A straight 3 addition circles
  python -m workbook_builder --pages A A A straight wavy  # Repeat pages

  # With font sizes (small, medium, large, extra-large)
  python -m workbook_builder --pages A:large straight circles A:large
  python -m workbook_builder --pages 1:extra-large 2:large 3:medium 4:small

  # Work on letter A today with progressive difficulty
  python -m workbook_builder --pages A:large straight addition:0-5:8 circles A:large addition:0-10:10 wavy A:large

  # Math with different number ranges
  python -m workbook_builder --pages addition:0-10 subtraction:0-20 addition:5-15
  python -m workbook_builder --pages addition:0-5:6 addition:0-10:12 addition:0-20:16

  # Activity selection (traditional)
  python -m workbook_builder --activities straight wavy zigzag --theme animals
  python -m workbook_builder --activities all --theme garden
  python -m workbook_builder --activities addition subtraction --math-range 0-10 --problems 12
        """
    )

    parser.add_argument(
        "--activities",
        nargs="+",
        default=None,
        help="Activity types to include (default: all). Options: all, straight, wavy, zigzag, diagonals, loops, circles, squares, triangles, pentagons, hexagons, octagons, ovals, rectangles, trapezoids, diamonds, spirals, addition, subtraction, spelling, colour, numbers, letters"
    )

    parser.add_argument(
        "--pages",
        nargs="+",
        default=None,
        help="Specify exact page order. Use: letter (A, A:large), number (3, 3:small), activity name, or math with difficulty (addition:easy, subtraction:0-10:8). Font sizes: small/medium/large/extra-large. Can repeat pages. Example: --pages A:large straight addition:easy circles"
    )

    parser.add_argument(
        "--theme",
        type=str,
        default="animals",
        choices=available_themes(),
        help=f"Theme for decorations (default: animals). Options: {', '.join(available_themes())}"
    )

    parser.add_argument(
        "--numbers",
        nargs="*",
        default=None,
        help="Numbers to include (0-9 or 'all'). If flag is present with no values, defaults to 'all'"
    )

    parser.add_argument(
        "--letters",
        nargs="*",
        default=None,
        help="Letters to include (A-Z, a-z, 'all' for uppercase, 'all-lower' for lowercase, 'all-both' for both). If flag is present with no values, defaults to 'all'"
    )

    parser.add_argument(
        "--rows",
        type=int,
        default=5,
        choices=range(3, 7),
        help="Number of rows per page (default: 5, range: 3-6)"
    )

    parser.add_argument(
        "--line-thickness",
        type=float,
        default=3.0,
        help="Guide line thickness in points (default: 3.0, range: 2.0-5.0)"
    )

    parser.add_argument(
        "--guide-style",
        type=str,
        default="dashed",
        choices=["dashed", "dotted", "solid"],
        help="Guide line style (default: dashed)"
    )

    parser.add_argument(
        "--output", "-o",
        type=str,
        default=None,
        help="Output PDF filename (default: worksheet_<theme>.pdf)"
    )

    parser.add_argument(
        "--math-range",
        type=str,
        default="0-10",
        help="Number range for addition/subtraction problems in format min-max (default: 0-10, range: 0-100)"
    )

    parser.add_argument(
        "--problems",
        type=int,
        default=12,
        help="Number of math problems per page (default: 12, range: 6-20)"
    )

    parser.add_argument(
        "--numbers-size",
        type=str,
        default="medium",
        choices=["small", "medium", "large", "extra-large"],
        help="Font size for number tracing (default: medium)"
    )

    parser.add_argument(
        "--letters-size",
        type=str,
        default="medium",
        choices=["small", "medium", "large", "extra-large"],
        help="Font size for letter tracing (default: medium)"
    )

    parser.add_argument(
        "--min-word-length",
        type=int,
        default=None,
        help="Minimum word length for spelling activity (default: no minimum)"
    )

    parser.add_argument(
        "--max-word-length",
        type=int,
        default=None,
        help="Maximum word length for spelling activity (default: no maximum)"
    )

    parser.add_argument(
        "--colour-folder",
        type=str,
        default=None,
        choices=["shapes", "animals", "objects", "nature", "custom"],
        help="Specific folder to use for coloring images (default: all folders)"
    )

    args = parser.parse_args()

    # Set default for activities if --pages not specified
    if args.activities is None and args.pages is None:
        args.activities = ["all"]

    # Validate that only one of --pages or --activities is used
    if args.pages is not None and args.activities is not None:
        parser.error("Cannot use --pages with --activities. Choose one method.")

    # Handle --numbers with no values (defaults to all)
    if args.numbers is not None and len(args.numbers) == 0:
        args.numbers = list(range(10))
    elif args.numbers is not None:
        # Parse and expand numbers
        expanded_numbers = []
        for n in args.numbers:
            result = parse_number_arg(n)
            if isinstance(result, list):
                expanded_numbers.extend(result)
            else:
                expanded_numbers.append(result)
        args.numbers = expanded_numbers

    # Handle --letters with no values (defaults to all)
    if args.letters is not None and len(args.letters) == 0:
        args.letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    elif args.letters is not None:
        # Parse and expand letters
        expanded_letters = []
        for letter in args.letters:
            result = parse_letter_arg(letter)
            if isinstance(result, list):
                expanded_letters.extend(result)
            else:
                expanded_letters.append(result)
        args.letters = expanded_letters

    # Validate line thickness
    if not 2.0 <= args.line_thickness <= 5.0:
        parser.error("--line-thickness must be between 2.0 and 5.0")

    # Validate problems count
    if not 6 <= args.problems <= 20:
        parser.error("--problems must be between 6 and 20")

    # Validate math range format using shared validator
    if args.math_range:
        try:
            parse_numeric_range(args.math_range, min_val=0, max_val=100, context="--math-range")
        except ValueError as e:
            parser.error(str(e))

    try:
        output_path = generate(args)
        print(f"Successfully generated: {output_path}")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
