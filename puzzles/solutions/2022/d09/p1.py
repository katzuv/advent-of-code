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


def get_visited_positions_amount(
    steps: Iterator[tuple[int, int]], knots_amount: int
) -> int:
    """
    :param steps: sequence of steps, one by one
    :param knots_amount: amount of knots in the rope
    :return: number of positions the tail of the rope visits at least once
    """
    knots = [Knot(0, 0) for _ in range(knots_amount)]
    head = knots[0]
    tail = knots[-1]
    visited_positions = set()
    for step in steps:
        head.move(step)
        for index in range(1, knots_amount):
            # Move each knot according to the knot it follows.
            knots[index].move_to_other(knots[index - 1])
        visited_positions.add((tail.row, tail.column))
    return len(visited_positions)


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
