import sys
from typing import Iterator

import consts


def get_steps(input_text: str) -> Iterator[tuple[int, int]]:
    """
    :param input_text: puzzle input
    :return: sequence of steps, one by one
    """
    steps = []
    for step_count in input_text.splitlines():
        direction, count = step_count.split()
        step = consts.DIRECTION_TO_STEP[direction]
        count = int(count)
        yield from count * [step]
    return tuple(steps)


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
