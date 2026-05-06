import sys


def get_banks(input_text: str) -> list[list[int]]:
    return [list(map(int, line)) for line in input_text.splitlines()]


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        print(
            "Warning: No input provided", file=sys.stderr
        )  # Don't crash if no input was passed through command line arguments.
