from pathlib import Path
from typing import Union

REQUIRED_SUM = 2020
INPUT_FILE_PATH = Path('..', 'inputs', '1.txt')


def get_numbers_from_input(path: Union[str, Path] = INPUT_FILE_PATH) -> list[int]:
    if isinstance(path, str):
        path = Path(path)
    return list(map(int, path.read_text().splitlines()))


def get_required_product_two_numbers(entries: list[int]) -> int:
    for number in entries:
        if (REQUIRED_SUM - number) in entries:
            return number * (REQUIRED_SUM - number)
    raise ValueError('There is no pair of numbers where the condition can be met')


def main():
    numbers = get_numbers_from_input()
    product = get_required_product_two_numbers(numbers)
    print(f'Product of the two entries that add up to {REQUIRED_SUM}: {product}')


if __name__ == '__main__':
    main()
