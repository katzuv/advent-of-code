import itertools
import sys


def get_reports(input_text: str) -> list[tuple[int, ...]]:
    return [tuple(map(int, line.split())) for line in input_text.splitlines()]


def is_report_safe(report: tuple[int, ...]) -> bool:
    increasing = (report[1] - report[0]) > 0
    for current_level, next_level in itertools.pairwise(report):
        difference = next_level - current_level
        if (difference > 0) != increasing:  # Direction changed.
            return False
        if not (1 <= abs(difference) <= 3):  # Difference is not in range.
            return False
    return True


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
