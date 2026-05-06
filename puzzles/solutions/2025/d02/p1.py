import math
import sys


def get_ranges(input_text: str) -> list[range]:
    ranges = []
    for ids_range in input_text.split(","):
        start, end = map(int, ids_range.split("-"))
        ranges.append(range(start, end + 1))
    return ranges


def get_digits_amount(number: int) -> int:
    return int(math.log10(number)) + 1


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        print(
            "Warning: No input provided", file=sys.stderr
        )  # Don't crash if no input was passed through command line arguments.
