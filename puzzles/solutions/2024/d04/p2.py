import sys

from p1 import Matrix


def get_all_a_locations(matrix: Matrix) -> list[tuple[int, int]]:
    return [
        (row, column)
        for row, column in itertools.product(range(len(matrix)), range(len(matrix[0])))
        if matrix[row][column] == "A"
    ]


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
