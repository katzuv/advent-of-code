from pathlib import Path


COMMAND_FILE_SUFFIX = '_command.py'
COMMANDS_FILES_PATHS = tuple(Path('commands').glob(f'*{COMMAND_FILE_SUFFIX}'))
# Linux and Windows separators to module notation, including upper package and accessing module inside package.
SEPARATORS_TO_MODULE_NOTATION = {'../': '..', '/': '.', '..\\': '..', '\\': '.'}


class CliConstants:
    CONTEXT = {'help_option_names': ['-h', '--help']}
