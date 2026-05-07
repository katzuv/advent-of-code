import sys

input_example = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
""".strip()


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    puzzle_input = sys.argv[1] if len(sys.argv) > 1 else input_example
    print(get_answer(puzzle_input))
