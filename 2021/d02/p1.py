import collections
import re
from pathlib import Path


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
