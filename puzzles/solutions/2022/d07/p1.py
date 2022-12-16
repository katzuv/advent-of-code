import sys
from typing import Sequence

import consts
import input_parsing
from directory import Directory


def get_commands(input_text: str) -> tuple[str, ...]:
    """
    :param input_text: puzzle input
    :return: tuple of commands from the terminal output
    """
    # Remove the first `$` so we don't have an empty string after running `split()`.
    input_text = input_text[1:]
    # First command is `cd /` which we can skip.
    commands = input_text.split(consts.COMMANDS_SEPARATOR)[1:]
    return tuple(command.strip() for command in commands)


def build_filesystem(commands: Sequence[str]) -> Directory:
    """
    Build the filesystem according to the given commands and return the root directory.
    :param commands: commands output
    :return: root directory
    """
    root = Directory(consts.ROOT_DIRECTORY_SYMBOL)
    current_directory = root
    for command in commands:
        if command.startswith(consts.CHANGE_DIRECTORY_COMMAND):
            current_directory = input_parsing.get_next_directory(
                current_directory, command
            )
        elif command.startswith(consts.LIST_CONTENTS_COMMAND):
            input_parsing.handle_ls_command(current_directory, command)

    return root


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
