"""Validation utilities for CLI arguments and page specifications."""


def parse_numeric_range(range_str, min_val=0, max_val=100, context="range"):
    """Parse and validate a numeric range string in 'min-max' format.

    Args:
        range_str: String in format "min-max" (e.g., "0-10", "5-20")
        min_val: Minimum allowed value (default: 0)
        max_val: Maximum allowed value (default: 100)
        context: Description of what's being parsed (for error messages)

    Returns:
        tuple: (min_num, max_num) as integers

    Raises:
        ValueError: If format is invalid or values are out of bounds

    Examples:
        >>> parse_numeric_range("0-10")
        (0, 10)
        >>> parse_numeric_range("5-20", min_val=0, max_val=100)
        (5, 20)
    """
    # Check format has hyphen
    if "-" not in range_str:
        raise ValueError(
            f"Invalid {context} format: '{range_str}'. Expected format 'min-max' (e.g., '0-10')"
        )

    # Split and validate parts
    parts = range_str.split("-")
    if len(parts) != 2:
        raise ValueError(
            f"Invalid {context} format: '{range_str}'. Expected exactly one hyphen"
        )

    # Validate both parts are numeric
    if not parts[0].isdigit() or not parts[1].isdigit():
        raise ValueError(
            f"Invalid {context}: '{range_str}'. Both min and max must be numeric"
        )

    # Parse to integers
    min_num = int(parts[0])
    max_num = int(parts[1])

    # Validate bounds
    if not (min_val <= min_num <= max_val and min_val <= max_num <= max_val):
        raise ValueError(
            f"Invalid {context}: '{range_str}'. Values must be between {min_val} and {max_val}"
        )

    # Validate min <= max
    if min_num > max_num:
        raise ValueError(
            f"Invalid {context}: '{range_str}'. Minimum ({min_num}) cannot be greater than maximum ({max_num})"
        )

    return min_num, max_num
