import click

from consts import CliConstants


@click.group(context_settings=CliConstants.CONTEXT)
def cli():
    """
    Main CLI holding all Advent of Code related commands.

    For more information about Advent of Code, see https://adventofcode.com.
    """


if __name__ == '__main__':
    cli()
