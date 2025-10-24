import sys


def get_reports(input_text: str) -> list[tuple[int, ...]]:
    return [tuple(map(int, line.split())) for line in input_text.splitlines()]


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
