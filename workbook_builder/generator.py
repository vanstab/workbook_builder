"""PDF generator - orchestrates building the worksheet from CLI arguments."""

import string
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from .activities import ACTIVITY_REGISTRY, ALL_ACTIVITIES
from .activities.spelling import Spelling
from .activities.colour import Colour
from .activities.numbers import NumberTracing
from .activities.letters import LetterTracing
from .icons import get_theme
from .colors import parse_dash_style
from .validators import parse_numeric_range


def parse_page_spec(spec):
    """Parse a single page specification.

    Args:
        spec: Page specification string
            Examples:
            - "A", "3", "straight" (basic)
            - "addition:0-5" (math with range)
            - "subtraction:0-10:8" (math with range and problem count)
            - "addition:easy" (math with difficulty alias)

    Returns:
        Activity instance

    Raises:
        ValueError: If specification is invalid
    """
    # Import here to avoid circular dependency
    from .activities.addition import Addition
    from .activities.subtraction import Subtraction

    # Check if it's an activity name (without parameters)
    if spec in ACTIVITY_REGISTRY:
        return ACTIVITY_REGISTRY[spec]

    # Special handling for spelling - always create new instance
    if spec == "spelling":
        return Spelling()

    # Special handling for colour - always create new instance
    if spec == "colour":
        return Colour(images_per_page=1)

    # Handle colour:folder format (e.g., colour:shapes)
    if spec.startswith("colour:"):
        parts = spec.split(":")
        if len(parts) == 2:
            folder = parts[1]
            return Colour(images_per_page=1, folder=folder)
        else:
            raise ValueError(f"Invalid colour specification: {spec}. Use 'colour' or 'colour:foldername'")

    # Check if it's a single uppercase letter (A-Z)
    if len(spec) == 1 and spec in string.ascii_uppercase:
        return LetterTracing(spec, size="medium")

    # Check if it's a single lowercase letter (a-z)
    if len(spec) == 1 and spec in string.ascii_lowercase:
        return LetterTracing(spec, size="medium")

    # Check if it's a single digit (0-9)
    if len(spec) == 1 and spec.isdigit():
        return NumberTracing(int(spec), size="medium")

    # Check if it's a multi-digit number
    if spec.isdigit():
        num = int(spec)
        if 0 <= num <= 9:
            return NumberTracing(num, size="medium")
        else:
            raise ValueError(f"Number must be 0-9, got {num}")

    # Check for colon-separated format (letter:X, number:X, addition:range, etc.)
    if ":" in spec:
        parts = spec.split(":")
        type_part = parts[0]

        # Handle shorthand: A:large or 3:small (single char + size)
        if len(parts) == 2 and len(type_part) == 1:
            size = parts[1]
            # Check if it's a letter with size
            if type_part.isalpha():
                return LetterTracing(type_part, size=size)
            # Check if it's a number with size
            elif type_part.isdigit():
                return NumberTracing(int(type_part), size=size)

        type_part_lower = type_part.lower()

        # Handle letter:X or letter:X:size
        if type_part_lower == "letter":
            if len(parts) >= 2 and len(parts[1]) == 1 and parts[1].isalpha():
                letter = parts[1]
                size = parts[2] if len(parts) >= 3 else "medium"
                return LetterTracing(letter, size=size)
            else:
                raise ValueError(f"Invalid letter specification: {spec}")

        # Handle number:X or number:X:size
        elif type_part_lower == "number":
            if len(parts) >= 2 and parts[1].isdigit():
                num = int(parts[1])
                if 0 <= num <= 9:
                    size = parts[2] if len(parts) >= 3 else "medium"
                    return NumberTracing(num, size=size)
                else:
                    raise ValueError(f"Number must be 0-9, got {num}")
            else:
                raise ValueError(f"Invalid number specification: {spec}")

        # Handle addition:min-max or addition:min-max:problems
        elif type_part_lower == "addition":
            min_num = None
            max_num = None
            problems = None

            if len(parts) >= 2:
                # Parse and validate range using shared validator
                try:
                    min_num, max_num = parse_numeric_range(parts[1], min_val=0, max_val=100, context="math range")
                except ValueError as e:
                    raise ValueError(f"Invalid addition specification: {e}")

            if len(parts) >= 3:
                if parts[2].isdigit():
                    problems = int(parts[2])
                    if not 6 <= problems <= 20:
                        raise ValueError(f"Problems must be 6-20, got {problems}")
                else:
                    raise ValueError(f"Invalid problem count: {parts[2]}")

            return Addition(min_num=min_num, max_num=max_num, problems_per_page=problems)

        # Handle subtraction:min-max or subtraction:min-max:problems
        elif type_part_lower == "subtraction":
            min_num = None
            max_num = None
            problems = None

            if len(parts) >= 2:
                # Parse and validate range using shared validator
                try:
                    min_num, max_num = parse_numeric_range(parts[1], min_val=0, max_val=100, context="math range")
                except ValueError as e:
                    raise ValueError(f"Invalid subtraction specification: {e}")

            if len(parts) >= 3:
                if parts[2].isdigit():
                    problems = int(parts[2])
                    if not 6 <= problems <= 20:
                        raise ValueError(f"Problems must be 6-20, got {problems}")
                else:
                    raise ValueError(f"Invalid problem count: {parts[2]}")

            return Subtraction(min_num=min_num, max_num=max_num, problems_per_page=problems)

        # Handle spelling:min-max or spelling:min or spelling:max
        elif type_part_lower == "spelling":
            min_length = None
            max_length = None

            if len(parts) >= 2:
                # Check if it's a range like "3-5"
                if "-" in parts[1]:
                    range_parts = parts[1].split("-")
                    if len(range_parts) == 2 and range_parts[0].isdigit() and range_parts[1].isdigit():
                        min_length = int(range_parts[0])
                        max_length = int(range_parts[1])
                    else:
                        raise ValueError(f"Invalid word length range: {parts[1]}. Use format like 3-5")
                # Check if it's just a single number (treat as max)
                elif parts[1].isdigit():
                    max_length = int(parts[1])
                else:
                    raise ValueError(f"Invalid word length specification: {parts[1]}")

            return Spelling(min_length=min_length, max_length=max_length)

        else:
            raise ValueError(f"Unknown type in specification: {type_part_lower}")

    raise ValueError(f"Unknown page specification: {spec}. Use activity name (straight, circles, addition), letter (A-Z), number (0-9), or format like addition:0-5")


def build_page_list(args):
    """Build ordered list of Activity instances from CLI arguments.

    Args:
        args: argparse.Namespace with activities, pages, numbers, letters, etc.

    Returns:
        list of Activity instances in the order they should appear
    """
    pages = []

    # If --pages is specified, use that for exact page ordering
    if args.pages:
        for spec in args.pages:
            try:
                page = parse_page_spec(spec)
                pages.append(page)
            except ValueError as e:
                raise ValueError(f"Error parsing page specification '{spec}': {e}")
        return pages

    # Otherwise, use the legacy --activities approach
    activities = args.activities

    # Expand "all" to include all base activities
    if "all" in activities:
        activities = ALL_ACTIVITIES.copy()

    # Process each requested activity
    for activity_name in activities:
        if activity_name == "numbers":
            # Expand to one page per number
            numbers = args.numbers if args.numbers else list(range(10))
            numbers_size = getattr(args, 'numbers_size', 'medium') or 'medium'
            for num in numbers:
                pages.append(NumberTracing(num, size=numbers_size))
        elif activity_name == "letters":
            # Expand to one page per letter
            if args.letters:
                letters = args.letters
            else:
                letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
            letters_size = getattr(args, 'letters_size', 'medium') or 'medium'
            for letter in letters:
                pages.append(LetterTracing(letter, size=letters_size))
        elif activity_name == "spelling":
            # Create Spelling with min/max word length from args
            min_length = getattr(args, 'min_word_length', None)
            max_length = getattr(args, 'max_word_length', None)
            pages.append(Spelling(min_length=min_length, max_length=max_length))
        elif activity_name == "colour":
            # Create Colour with images_per_page and folder from args
            images_per_page = getattr(args, 'images_per_page', 1)
            colour_folder = getattr(args, 'colour_folder', None)
            pages.append(Colour(images_per_page=images_per_page, folder=colour_folder))
        elif activity_name in ACTIVITY_REGISTRY:
            # Standard activity
            pages.append(ACTIVITY_REGISTRY[activity_name])
        else:
            raise ValueError(f"Unknown activity: {activity_name}")

    # If --numbers was provided but "numbers" not in activities, add them
    if args.numbers is not None and "numbers" not in args.activities and "all" not in args.activities:
        numbers = args.numbers if args.numbers else list(range(10))
        numbers_size = getattr(args, 'numbers_size', 'medium') or 'medium'
        for num in numbers:
            pages.append(NumberTracing(num, size=numbers_size))

    # If --letters was provided but "letters" not in activities, add them
    if args.letters is not None and "letters" not in args.activities and "all" not in args.activities:
        letters = args.letters if args.letters else [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        letters_size = getattr(args, 'letters_size', 'medium') or 'medium'
        for letter in letters:
            pages.append(LetterTracing(letter, size=letters_size))

    return pages


def generate(args):
    """Generate the PDF worksheet from CLI arguments.

    Args:
        args: argparse.Namespace with all CLI arguments
    """
    # Build the page list
    pages = build_page_list(args)

    if not pages:
        raise ValueError("No activities selected. Use --activities to specify activities.")

    # Get theme
    theme = get_theme(args.theme)

    # Parse math range into min/max
    math_range = getattr(args, 'math_range', '0-10')
    try:
        min_num, max_num = parse_numeric_range(math_range, min_val=0, max_val=100, context="math range")
    except ValueError:
        # Fallback to default if parsing fails
        min_num = 0
        max_num = 10

    # Build layout dict
    layout = {
        "rows": args.rows,
        "thickness": args.line_thickness,
        "dash": parse_dash_style(args.guide_style),
        "min_num": min_num,
        "max_num": max_num,
        "problems_per_page": args.problems,
    }

    # Determine output filename
    if args.output:
        output_path = args.output
    else:
        output_path = f"worksheet_{args.theme}.pdf"

    # Create the PDF
    pdf = canvas.Canvas(output_path, pagesize=letter)

    # Render each page
    for i, activity in enumerate(pages):
        if i > 0:
            pdf.showPage()
        activity.render(pdf, i, len(pages), theme, layout)

    # Save the PDF
    pdf.save()

    return output_path
