from pathlib import Path


FIRST_AOC_YEAR = 2015

_PYTHON_FILE_EXTENSION = '.py'
COMMANDS_FILES_PATHS = tuple(Path('commands').glob(f'*{_PYTHON_FILE_EXTENSION}'))


class CliConstants:
    CONTEXT = {'help_option_names': ['-h', '--help']}
