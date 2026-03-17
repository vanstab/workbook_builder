"""Addition worksheet activity."""

from .math_base import MathActivity


class Addition(MathActivity):
    """Addition practice activity."""

    operation_symbol = "+"
    operation_name = "Addition"

    def _generate_problems(self, page_idx, min_num, max_num, count):
        """Generate unique addition problems deterministically.

        Args:
            page_idx: Page index for seeding
            min_num: Minimum number (0-100)
            max_num: Maximum number (0-100)
            count: Number of problems to generate

        Returns:
            list of (a, b, answer) tuples with no duplicates
        """
        # Deterministic pseudo-random based on page_idx
        # Using Linear Congruential Generator for reproducibility
        seed = (page_idx + 1) * 7919  # prime multiplier
        problems = []
        seen = set()  # Track (a, b) pairs - order matters, so (3, 2) != (2, 3)

        # Keep generating until we have enough unique problems
        max_attempts = count * 100  # Prevent infinite loop
        attempts = 0
        range_size = max_num - min_num + 1

        while len(problems) < count and attempts < max_attempts:
            attempts += 1

            # Generate two numbers using LCG
            seed = (seed * 1103515245 + 12345) & 0x7FFFFFFF
            a = min_num + (seed % range_size)

            seed = (seed * 1103515245 + 12345) & 0x7FFFFFFF
            b = min_num + (seed % range_size)

            # Check if this problem is unique (order matters)
            if (a, b) not in seen:
                seen.add((a, b))
                problems.append((a, b, a + b))

        return problems
