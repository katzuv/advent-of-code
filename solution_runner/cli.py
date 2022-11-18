import click

import commands
from consts import CliConstants


@click.group(context_settings=CliConstants.CONTEXT)
def cli() -> click.Group:
    """
    Main CLI holding all Advent of Code related commands.

    For more information about Advent of Code, see https://adventofcode.com.
    """


if __name__ == "__main__":
    cli.add_command(commands.setup)
    cli.add_command(commands.config)
    cli.add_command(commands.submit)
    cli()
