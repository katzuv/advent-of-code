import itertools
import sys

import input_parsing


def does_seed_exist(running_value: int, seeds_ranges: list[range]) -> bool:
    return any(running_value in seed_range for seed_range in seeds_ranges)


def get_answer(input_text: str) -> int:
    """Return the lowest location number hat corresponds to any of the initial seed numbers."""
    seeds_list, mappings = input_parsing.get_initial_data(input_text)
    seeds_ranges = input_parsing.get_seeds_ranges(seeds_list)
    mappings = input_parsing.reverse_mappings(mappings)

    for location_number in itertools.count(start=1):
        running_value = location_number
        for mapping_ranges in mappings:
            for source_range_start, source_range_end, difference in mapping_ranges:
                if source_range_start <= running_value < source_range_end:
                    running_value += difference
                    break
        print(location_number, running_value)
        if does_seed_exist(running_value, seeds_ranges):
            return running_value


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
