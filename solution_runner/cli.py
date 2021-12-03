import click

from consts import CliConstants


@click.group(context_settings=CliConstants.CONTEXT)
def cli():
    """
    Main CLI holding all Advent of Code related commands.

    For more information about Advent of Code, see https://adventofcode.com.
    """


@cli.command()
def setup():
    """Set up a solution: fetch input and create solution files."""


if __name__ == '__main__':
    cli()
