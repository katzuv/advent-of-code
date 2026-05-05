import sys

from p1 import get_turns


def get_answer(input_text: str):
    turns = get_turns(input_text)

    current_turn = 50

    visits_at_zero = 0


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        print(
            "Warning: No input provided", file=sys.stderr
        )  # Don't crash if no input was passed through command line arguments.
