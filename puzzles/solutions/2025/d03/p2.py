import sys

from p1 import get_banks

BATTERIES_AMOUNT = 12


def get_answer(input_text: str):
    banks = get_banks(input_text)
    max_joltages = 0
    for bank in banks:
        max_joltage = 0
        current_index = 0
        for digit_number in range(BATTERIES_AMOUNT):
            last_possible_index = 1 + digit_number - BATTERIES_AMOUNT
            if last_possible_index == 0:
                last_possible_index = len(bank)
            max_digit = max(bank[current_index:last_possible_index])
            current_index = bank.index(max_digit, current_index) + 1
            max_joltage += max_digit * 10 ** (BATTERIES_AMOUNT - digit_number - 1)
        max_joltages += max_joltage
    return max_joltages


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        print(
            "Warning: No input provided", file=sys.stderr
        )  # Don't crash if no input was passed through command line arguments.
