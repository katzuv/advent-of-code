import collections
import re
from pathlib import Path
from typing import Iterator

import directions


INPUT_FILE_PATH = Path('..', 'inputs', '2.txt')

DIRECTION = 'direction'
STEP_SIZE = 'step_size'

Command = collections.namedtuple('Command', (DIRECTION, STEP_SIZE))


def get_commands_from_input(input_text: str) -> list[Command]:
    """
    :param input_text: input test to process
    :return: commands from the input
    """
    commands = []
    for command in input_text.splitlines():
        match = re.match(fr'(?P<{DIRECTION}>forward|up|down) (?P<{STEP_SIZE}>\d+)', command)
        direction, step_size = match.groupdict().values()
        commands.append(Command(direction, int(step_size)))
    return commands


def get_position(commands: Iterator[Command], horizontal: int = 0, depth: int = 0) -> tuple[int, int]:
    """
    Get position the submarine would be at after completing the given commands.
    :param commands: list of command to follow
    :param horizontal: initial horizontal position, defaults to 0
    :param depth: initial depth, defaults to 0
    :return: horizontal and depth of the submarine after completing the given commands
    """
    for command in commands:
        step_size = command.step_size
        match command.direction:
            case directions.FORWARD:
                horizontal += step_size
            case directions.UP:
                depth -= step_size
            case directions.DOWN:
                depth += step_size

    return horizontal, depth
