from pathlib import Path


INPUT_FILE_PATH = Path('..', 'inputs', '2.txt')

DIRECTION = 'direction'
STEP_SIZE = 'step_size'


Command = dict[str, int]  # Dictionary including direction and step size.
