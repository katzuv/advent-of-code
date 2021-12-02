import collections
from pathlib import Path


INPUT_FILE_PATH = Path('..', 'inputs', '2.txt')

DIRECTION = 'direction'
STEP_SIZE = 'step_size'

Command = collections.namedtuple('Command', (DIRECTION, STEP_SIZE))

