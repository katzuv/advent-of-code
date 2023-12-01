import sys

import p1


DIGITS_NAMES_TO_NUMBERS = dict(
    zip(
        ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine"),
        (map(str, range(1, 10))),
    )
)


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
