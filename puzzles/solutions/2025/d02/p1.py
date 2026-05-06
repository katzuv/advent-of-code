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
    ranges = get_ranges(input_text)

    ids_sum = 0

    for current_range in ranges:
        start, end = current_range.start, current_range.stop
        start_digits_amount = get_digits_amount(start)

        if start_digits_amount % 2 != 0:
            start = 10**start_digits_amount
            if start > end:
                continue

        smallest_half_id = get_relevant_id_half(start, is_start=True)
        largest_half_id = get_relevant_id_half(end, is_start=False)
        for half_id in range(smallest_half_id, largest_half_id + 1):
            half_digits_amount = get_digits_amount(half_id)
            # Example: 13 -> 13 * 100 + 13 = 1313
            full_id = half_id * (10**half_digits_amount + 1)
            if full_id in current_range:
                ids_sum += full_id

    return ids_sum


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        print(
            "Warning: No input provided", file=sys.stderr
        )  # Don't crash if no input was passed through command line arguments.
