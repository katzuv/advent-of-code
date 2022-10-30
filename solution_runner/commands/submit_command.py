import click

from . import consts
from .defaults_and_choices import get_default_year


_default_year = get_default_year()


@click.command(name='submit')
@click.option('-y', '--year', type=click.IntRange(consts.FIRST_AOC_YEAR, _default_year), default=_default_year,
              show_default=f'last year: {_default_year}', help='year of puzzle setting up solution for')
@click.option('-d', '--day', type=consts.ADVENT_DAYS_RANGE, required=True, help='day of puzzle to submit')
@click.option('-p', '--part', type=click.Choice(('1', '2')), required=True, help='puzzle part to submit')
def command(year: int, day: int, part: int):
    """Submit solution."""
    year = str(year)
    day = str(day)