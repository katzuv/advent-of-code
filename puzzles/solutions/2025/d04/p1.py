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


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    puzzle_input = sys.argv[1] if len(sys.argv) > 1 else example_input
    print(get_answer(puzzle_input))
