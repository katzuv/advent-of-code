from pathlib import Path


INPUT_FILE_PATH = Path('..', 'inputs', '2.txt')

DIRECTION = 'direction'


Command = dict[str, int]  # Dictionary including direction and step size.
