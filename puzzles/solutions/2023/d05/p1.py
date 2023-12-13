import sys


def get_map_ranges(lines: list[str]) -> dict[int, int]:
    mapping = {}
    for line in lines:
        destination_range_start, source_range_start, range_length = map(
            int, line.split()
        )
        source_numbers = range(source_range_start, source_range_start + range_length)
        destination_numbers = range(
            destination_range_start, destination_range_start + range_length
        )

        mapping |= zip(source_numbers, destination_numbers)
    return mapping


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
