import itertools
import sys


def get_banks(input_text: str) -> list[list[int]]:
    return [list(map(int, line)) for line in input_text.splitlines()]


def get_answer(input_text: str):
    banks = get_banks(input_text)
    max_joltages = 0
    for bank in banks:
        bank_joltages = itertools.combinations(bank, 2)
        max_joltage = max(bank_joltages)
        max_joltages += max_joltage[0] * 10 + max_joltage[1]
    return max_joltages


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        print(
            "Warning: No input provided", file=sys.stderr
        )  # Don't crash if no input was passed through command line arguments.
