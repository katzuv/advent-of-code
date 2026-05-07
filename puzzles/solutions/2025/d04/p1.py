import itertools
import sys

example_input = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
""".strip()

PAPER_ROLL = "@"
MAX_ADJACENT_PAPER_ROLLS = 3

Grid = list[list[str]]
Position = tuple[int, int]


def get_grid(input_text: str) -> Grid:
    return [list(line) for line in input_text.splitlines()]


def get_adjacent_rolls_number(grid, row, column):
    min_row = max(row - 1, 0)
    max_row = min(row + 1, len(grid) - 1)
    min_column = max(column - 1, 0)
    max_column = min(column + 1, len(grid[0]) - 1)
    return (
        sum(
            grid[current_row][current_column] == PAPER_ROLL
            for current_row, current_column in itertools.product(
                range(min_row, max_row + 1), range(min_column, max_column + 1)
            )
        )
        # Exclude the cell we're counting adjacent around.
        - (grid[row][column] == PAPER_ROLL)
    )


def get_accessible_rolls(grid: list[str]) -> list[Position]:
    return [
        (row, column)
        for row, column in itertools.product(range(len(grid)), range(len(grid[0])))
        if (
            grid[row][column] == PAPER_ROLL
            and get_adjacent_rolls_number(grid, row, column) <= MAX_ADJACENT_PAPER_ROLLS
        )
    ]


def get_answer(input_text: str):
    grid = get_grid(input_text)
    return len(get_accessible_rolls(grid))


if __name__ == "__main__":
    puzzle_input = sys.argv[1] if len(sys.argv) > 1 else example_input
    print(get_answer(puzzle_input))
