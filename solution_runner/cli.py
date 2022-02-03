import os
from pathlib import Path
from typing import Iterator

import click

import consts
from consts import CliConstants
from utils import get_module_from_filepath


@click.group(context_settings=CliConstants.CONTEXT)
def cli() -> click.Group:
    """
    Main CLI holding all Advent of Code related commands.

    For more information about Advent of Code, see https://adventofcode.com.
    """


def _add_commands_to_cli(cli: click.Group, commands_files_paths: Iterable[Path]) -> click.Group:
    """
    :param cli: click.Group object
    :param commands_files_paths: path to directory containing Python files with Python subcommands
    :return: CLI with added subcommands
    """
    file_directory = Path(__file__).parent
    current_directory = Path.cwd()
    os.chdir(file_directory)
    for filepath in commands_files_paths:
        module = get_module_from_filepath(filepath)
        cli.add_command(module.command)
    os.chdir(current_directory)


def main():
    """Add subcommands to the solution runner CLI and run it."""
    _add_commands_to_cli(cli, consts.COMMANDS_FILES_PATHS)
    cli()


if __name__ == '__main__':
    main()
