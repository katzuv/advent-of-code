import sys

import p1


def get_answer(input_text: str):
    """Return the number of positions the tail of the rope visits at least once, when the rope has total 10 knots."""
    steps = p1.get_steps(input_text)
    return p1.get_visited_positions_amount(steps, 10)


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
