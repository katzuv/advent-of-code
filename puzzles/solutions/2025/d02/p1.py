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
    Return the prefix used to build the nearest repeated-half ID bound.

    The number is treated as having an even number of digits and is split into
    two equal-length halves: ``first_half`` and ``second_half``. The caller
    then reconstructs a full ID by repeating the returned half, e.g. ``13``
    becomes ``1313``.

    For a start bound, return the smallest half whose repeated form is greater
    than or equal to ``number``. If ``first_half < second_half``, repeating
    ``first_half`` would produce a value below ``number``, so the half is
    incremented.

    For an end bound, return the largest half whose repeated form is less than
    or equal to ``number``. If ``first_half > second_half``, repeating
    ``first_half`` would produce a value above ``number``, so the half is
    decremented.

    Example: ``1234`` splits into ``12 | 34``. As a start bound, this returns
    ``13`` (so the first candidate ID is ``1313``). As an end bound, ``1299``
    splits into ``12 | 99`` and returns ``12`` (so the last candidate ID is
    ``1212``).
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
        start, end = current_range.start, current_range.stop - 1
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
