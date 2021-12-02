from typing import Iterator

import directions
from p1 import Command


def get_position(commands: Iterator[Command], horizontal: int = 0, depth: int = 0, aim: int = 0) -> tuple[int, int]:
    """
    Get position the submarine would be at after completing the given commands.
    :param commands: list of command to follow
    :param horizontal: initial horizontal position, defaults to 0
    :param depth: initial depth, defaults to 0
    :param aim: initial aim, defaults to 0
    :return: horizontal and depth of the submarine after completing the given commands
    """
    for command in commands:
        step = command.step
        match command.direction:
            case directions.FORWARD:
                horizontal += step
                depth += aim * step
            case directions.DOWN:
                aim += step
            case directions.UP:
                aim -= step

    return horizontal, depth
