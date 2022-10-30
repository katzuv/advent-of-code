import click

from . import consts
from .defaults_and_choices import get_default_year


_default_year = get_default_year()


@click.command(name='submit')
@click.option('-y', '--year', type=click.IntRange(consts.FIRST_AOC_YEAR, _default_year), default=_default_year,
              show_default=f'last year: {_default_year}', help='year of puzzle setting up solution for')
def command(year: int):
    """Submit solution."""
    pass
