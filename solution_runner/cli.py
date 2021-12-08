import click

import consts
from consts import CliConstants
from defaults_and_choices import get_default_year


@click.group(context_settings=CliConstants.CONTEXT)
def cli() -> click.Group:
    """
    Main CLI holding all Advent of Code related commands.

    For more information about Advent of Code, see https://adventofcode.com.
    """


@cli.command()
@click.option('-y', '--year', type=click.IntRange(consts.FIRST_AOC_YEAR, get_default_year()),
              default=get_default_year(), help='year of challenge setting up solution for')
@click.option('-d', '--day', type=click.IntRange(1, 25), help='day of challenge setting up solution for')
@click.option('--use_cache/--ignore_cache', default=True, help='whether to use cached input file [default: true]')
def setup(year: int, day: int, use_cache: bool):
    """Set up a solution: fetch input and create solution files."""


if __name__ == '__main__':
    cli()
