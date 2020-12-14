import itertools
from pathlib import Path

INPUT_FILE_PATH = Path('..', 'inputs', '9.txt')

PREAMBLE_LENGTH = 25


def get_numbers_from_input(input_text: str) -> list[int]:
    return [int(number) for number in input_text.splitlines()]


def is_number_valid(number: int, numbers: list[int]) -> bool:
    for first, second in itertools.combinations(numbers, 2):
        if number == first + second:
            return True

    return False


def get_first_invalid_number(numbers: list[int]) -> int:
    for i, number in enumerate(numbers[PREAMBLE_LENGTH:]):
        preamble = numbers[i:i + PREAMBLE_LENGTH]
        if not is_number_valid(number, preamble):
            return number


def main():
    input_text = INPUT_FILE_PATH.read_text()
    numbers = get_numbers_from_input(input_text)
    number = get_first_invalid_number(numbers)

    print(f'First number which is not a sum of two of the {PREAMBLE_LENGTH} numbers before it: {number}')


if __name__ == '__main__':
    main()
