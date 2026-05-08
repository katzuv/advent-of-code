import functools
import operator
import re
import sys
from collections.abc import Callable

input_example = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

Problem = tuple[list[int], Callable[[int, int], int]]

OPERATIONS_MAP = {"+": operator.add, "*": operator.mul}


def get_problems(input_text: str) -> list[Problem]:
    lines = input_text.splitlines()
    number_lines = lines[:-1]
    return [
        (
            [int(line[m.start() : m.end()]) for line in number_lines],
            OPERATIONS_MAP[m.group().strip()],
        )
        for m in re.finditer(r"[+*]\s*", lines[-1])
    ]


def get_answer(input_text: str):
    problems = get_problems(input_text)
    return sum(
        functools.reduce(operation, numbers) for (numbers, operation) in problems
    )


if __name__ == "__main__":
    puzzle_input = sys.argv[1] if len(sys.argv) > 1 else input_example
    print(get_answer(puzzle_input))
