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

Grid = list[list[str]]


def get_grid(input_text: str) -> Grid:
    return [list(line) for line in input_text.splitlines()]

def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    puzzle_input = sys.argv[1] if len(sys.argv) > 1 else example_input
    print(get_answer(puzzle_input))
