import click

import consts
from defaults_and_choices import get_default_year


@click.command(name='setup')
@click.option('-y', '--year', type=click.IntRange(consts.FIRST_AOC_YEAR, get_default_year()),
              default=get_default_year(), help='year of challenge setting up solution for')
@click.option('-d', '--day', type=click.IntRange(1, 25), required=True, help='day of challenge setting up solution for')
@click.option('--use_cache/--ignore_cache', default=True, help='whether to use cached input file [default: true]')
def command(year: int, day: int, should_use_cache: bool):
    """Set up a solution: fetch input and create solution files."""
