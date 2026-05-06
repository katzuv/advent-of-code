import sys


def get_banks(input_text: str) -> list[list[int]]:
    return [list(map(int, line)) for line in input_text.splitlines()]


def get_answer(input_text: str):
    banks = get_banks(input_text)
    max_joltages = 0
    for bank in banks:
        max_joltage = 0
        for first_index, first_joltage in enumerate(bank):
            for _, second_joltage in enumerate(bank[first_index + 1 :]):
                if (joltage := first_joltage * 10 + second_joltage) > max_joltage:
                    max_joltage = joltage
        max_joltages += max_joltage
    return max_joltages


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        print(
            "Warning: No input provided", file=sys.stderr
        )  # Don't crash if no input was passed through command line arguments.
