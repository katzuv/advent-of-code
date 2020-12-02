import itertools

from p1 import REQUIRED_SUM, get_numbers_from_input


def get_required_product_three_numbers(entries: list[int]) -> int:
    for first, second in itertools.product(entries, entries):
        if (REQUIRED_SUM - first - second) in entries:
            return first * second * (REQUIRED_SUM - first - second)
    raise ValueError('There is no thrice of numbers where the condition can be met')


def main():
    numbers = get_numbers_from_input()
    product = get_required_product_three_numbers(numbers)
    print(f'Product of the three entries that add up to {REQUIRED_SUM}: {product}')


if __name__ == '__main__':
    main()
