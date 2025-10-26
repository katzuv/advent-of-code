import re
import sys


def get_products_sum(input_text: str) -> int:
    multiplications = re.findall(r"mul\(\d+,\d+\)", input_text)
    result = 0
    for multiplication in multiplications:
        a, b = map(int, re.findall("\d+", multiplication))
        result += a * b
    return result


def get_answer(input_text: str) -> int:
    return get_products_sum(input_text)


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
