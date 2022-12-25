import sys
from typing import Iterator


def get_instructions(input_text: str) -> Iterator[tuple[str, tuple[int, ...]]]:
    """
    :param input_text: puzzle input
    :return: generator of instructions and their parameters
    """
    for line in input_text.splitlines():
        instruction, *parameters = line.split()
        yield instruction, tuple(map(int, parameters))


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
