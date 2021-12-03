import click

import consts
from consts import CliConstants
from defaults_and_choices import get_default_year


@click.group(context_settings=CliConstants.CONTEXT)
def cli():
    """
    Main CLI holding all Advent of Code related commands.

    For more information about Advent of Code, see https://adventofcode.com.
    """


@cli.command()
@click.option('-y', '--year', type=click.IntRange(consts.FIRST_AOC_YEAR, get_default_year()),
              default=get_default_year(), help='year of challenge setting up solution for')
def setup(year: int):
    """Set up a solution: fetch input and create solution files."""


if __name__ == '__main__':
    cli()
