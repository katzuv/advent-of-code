import sys


def get_banks(input_text: str) -> list[list[int]]:
    return [list(map(int, line)) for line in input_text.splitlines()]


def get_answer(input_text: str):
    banks = get_banks(input_text)
    max_joltages = 0
    for bank in banks:
        tens_digit = max(bank[:-1])
        tens_digit_first_index = bank.index(tens_digit)
        ones_digit = max(bank[tens_digit_first_index + 1 :])
        max_joltages += tens_digit * 10 + ones_digit
    return max_joltages


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        print(
            "Warning: No input provided", file=sys.stderr
        )  # Don't crash if no input was passed through command line arguments.
