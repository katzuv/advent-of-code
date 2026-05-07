import copy
import sys

import p1

EMPTY_CELL = "."


def clean_accessed_rolls(
    grid: p1.Grid, accessible_rolls_positions: list[p1.Position]
) -> p1.Grid:
    grid = copy.deepcopy(grid)
    for row, column in accessible_rolls_positions:
        grid[row][column] = "."
    return grid


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        print(
            "Warning: No input provided", file=sys.stderr
        )  # Don't crash if no input was passed through command line arguments.
