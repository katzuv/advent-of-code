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
    grid = p1.get_grid(input_text)
    total_accessible_rolls = 0
    while True:
        accessible_rolls = p1.get_accessible_rolls(grid)
        if not accessible_rolls:
            break
        total_accessible_rolls += len(accessible_rolls)
        grid = clean_accessed_rolls(grid, accessible_rolls)
    return total_accessible_rolls


if __name__ == "__main__":
    puzzle_input = sys.argv[1] if len(sys.argv) > 1 else p1.example_input
    print(get_answer(puzzle_input))
