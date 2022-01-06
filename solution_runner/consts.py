from pathlib import Path


COMMAND_FILE_SUFFIX = '_command.py'
_COMMANDS_DIRECTORY_PATH = Path(__file__).parent / Path('commands')
COMMANDS_FILES_PATHS = tuple(_COMMANDS_DIRECTORY_PATH.glob(f'*{COMMAND_FILE_SUFFIX}'))
# Linux and Windows separators to module notation, including upper package and accessing module inside package.
SEPARATORS_TO_MODULE_NOTATION = {'../': '..', '/': '.', '..\\': '..', '\\': '.'}


class CliConstants:
    CONTEXT = {'help_option_names': ['-h', '--help']}
