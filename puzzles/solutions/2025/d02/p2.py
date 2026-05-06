import sys

import p1


def get_answer(input_text: str):
    ranges = p1.get_ranges(input_text)
    max_digits_amount_in_half_id = (
        p1.get_digits_amount(max(r.stop for r in ranges)) // 2
    )

    base_sequences_by_length = {
        length + 1: tuple(map(str, range(10**length, 10 ** (length + 1))))
        for length in range(max_digits_amount_in_half_id + 1)
    }.items()

    invalid_ids = set()

    for current_range in ranges:
        start_length, end_lengths = map(
            p1.get_digits_amount, (current_range.start, current_range.stop)
        )
        ids_possible_lengths = range(start_length, end_lengths + 1)
        max_sequence_length = max(ids_possible_lengths) // 2

        for length, base_sequences in base_sequences_by_length:
            if length > max_sequence_length:
                # The base sequences are sorted by length, so we can safely break here.
                # For example: If the number is 7 digits long, 4+ long base sequences can't build it.
                break

            # We start from 2 because an ID is invalid if it's made only of a sequence at least twice.
            for multiplier in range(2, max(ids_possible_lengths) + 1):
                if multiplier * length not in ids_possible_lengths:
                    continue
                for base_sequence in base_sequences:
                    current_id = int(base_sequence * multiplier)
                    if current_id in current_range:
                        invalid_ids.add(current_id)

    return sum(invalid_ids)


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        print(
            "Warning: No input provided", file=sys.stderr
        )  # Don't crash if no input was passed through command line arguments.
