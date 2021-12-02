import collections
import re
from pathlib import Path
from typing import Iterator

import directions


INPUT_FILE_PATH = Path('..', 'inputs', '2.txt')

DIRECTION = 'direction'
STEP = 'step'

Command = collections.namedtuple('Command', (DIRECTION, STEP))


def get_commands_from_input(input_text: str) -> list[Command]:
    """
    :param input_text: input test to process
    :return: commands from the input
    """
    commands = []
    for command in input_text.splitlines():
        match = re.match(fr'(?P<{DIRECTION}>forward|down|up) (?P<{STEP}>\d+)', command)
        direction, step = match.groupdict().values()
        commands.append(Command(direction, int(step)))
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
        step = command.step
        match command.direction:
            case directions.FORWARD:
                horizontal += step
            case directions.DOWN:
                depth += step
            case directions.UP:
                depth -= step

    return horizontal, depth


def main():
    input_text = INPUT_FILE_PATH.read_text()
    measurements = get_commands_from_input(input_text)

    horizontal_position, depth = get_position(measurements)
    product = horizontal_position * depth
    print(f"Product of the submarine's positional position with its depth: {product}")


if __name__ == '__main__':
    main()
