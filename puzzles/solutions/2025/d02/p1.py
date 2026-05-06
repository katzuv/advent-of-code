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


def get_relevant_id_half(number: int, *, is_start: bool) -> int:
    """
    Return the half of the relevant end ID.

    :return: If this is the start ID, return the smallest ID after this, which is a sequence of two numbers after the
    ID. If this is the end ID, return the largest ID before this, which is a sequence of two numbers after the ID.
    """
    digits_amount = get_digits_amount(number)
    half_digits_amount = digits_amount // 2
    split_divisor = 10**half_digits_amount
    first_half, second_half = divmod(number, split_divisor)

    if is_start and first_half < second_half:
        first_half += 1
    elif not is_start and first_half > second_half:
        first_half -= 1

    return first_half


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        print(
            "Warning: No input provided", file=sys.stderr
        )  # Don't crash if no input was passed through command line arguments.
