from pathlib import Path


_PYTHON_FILE_EXTENSION = '.py'
COMMANDS_FILES_PATHS = tuple(Path('commands').glob(f'*{_PYTHON_FILE_EXTENSION}'))
# Linux and Windows separators to module notation, including upper package and accessing module inside package.
SEPARATORS_TO_MODULE_NOTATION = {'../': '..', '/': '.', '..\\': '..', '\\': '.'}


class CliConstants:
    CONTEXT = {'help_option_names': ['-h', '--help']}
