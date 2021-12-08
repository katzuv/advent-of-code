from pathlib import Path
from typing import Iterator

import click

import consts
from consts import CliConstants
from solution_runner.modules_utils import get_module_from_filepath


@click.group(context_settings=CliConstants.CONTEXT)
def cli() -> click.Group:
    """
    Main CLI holding all Advent of Code related commands.

    For more information about Advent of Code, see https://adventofcode.com.
    """


def _add_commands_to_cli(cli: click.Group, commands_files_paths: Iterator[Path]) -> click.Group:
    """
    :param cli: click.Group object
    :param commands_files_paths: path to directory containing Python files with Python subcommands
    :return: CLI with added subcommands
    """
    for filepath in commands_files_paths:
        module = get_module_from_filepath(filepath)
        cli.add_command(module.command)


if __name__ == '__main__':
    cli()
