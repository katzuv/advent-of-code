from typing import Iterator

import directions
from p1 import INPUT_FILE_PATH, get_commands_from_input, Command


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


def main():
    input_text = INPUT_FILE_PATH.read_text()
    measurements = get_commands_from_input(input_text)

    horizontal_position, depth = get_position(measurements)
    product = horizontal_position * depth
    print(f"Product of the submarine's positional position with its depth: {product}")


if __name__ == '__main__':
    main()
