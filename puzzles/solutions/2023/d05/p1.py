import math
import sys
import input_parsing


def get_answer(input_text: str) -> int:
    """Return the lowest location number hat corresponds to any of the initial seed numbers."""
    initial_seeds, mappings = input_parsing.get_initial_data(input_text)
    lowest_location_number = math.inf
    for seed in initial_seeds:
        running_value = seed
        for name, mapping_ranges in mappings.items():
            for source_range_start, source_range_end, difference in mapping_ranges:
                if source_range_start <= running_value <= source_range_end:
                    running_value += difference
                    break
        lowest_location_number = min(lowest_location_number, running_value)

    return lowest_location_number


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
