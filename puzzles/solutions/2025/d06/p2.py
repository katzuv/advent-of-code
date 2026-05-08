import re
import sys

import p1


def transpose_numbers(number_lines: list[str]) -> list[list[int]]:
    columns_count = len(number_lines[0])
    number_lines = [
        [line[column] for line in number_lines] for column in range(columns_count)
    ]
    transposed_number_lines = [[]]
    for line in number_lines:
        try:
            transposed_number_lines[-1].append(int("".join(line)))
        except ValueError:
            # Whitespace row, create a new Problem.
            transposed_number_lines.append([])

    return transposed_number_lines


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    puzzle_input = sys.argv[1] if len(sys.argv) > 1 else p1.input_example
    print(get_answer(puzzle_input))
