import itertools
import sys

from p1 import Matrix


def get_all_a_locations(matrix: Matrix) -> list[tuple[int, int]]:
    return [
        (row, column)
        for row, column in itertools.product(
            range(1, len(matrix) - 1), range(1, len(matrix[0]) - 1)
        )
        if matrix[row][column] == "A"
    ]


def is_a_x_mas(matrix, location: tuple[int, int]) -> bool:
    row, column = location
    surrounding = (
        matrix[row - 1][column - 1],
        matrix[row + 1][column - 1],
        matrix[row + 1][column + 1],
        matrix[row - 1][column + 1],
    )
    return any("".join(surrounding[i:] + surrounding[:i]) == "SSMM" for i in range(4))


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
