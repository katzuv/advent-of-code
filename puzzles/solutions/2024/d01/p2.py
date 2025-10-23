import collections
import sys

from p1 import get_location_id_lists


def get_answer(input_text: str) -> int:
    first, second = get_location_id_lists(input_text)
    histogram = collections.Counter(second)
    return sum(number * histogram[number] for number in first)


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
