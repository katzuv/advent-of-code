import click

import consts
from defaults_and_choices import get_default_year


@click.command(name='setup')
@click.option('-y', '--year', type=click.IntRange(consts.FIRST_AOC_YEAR, get_default_year()),
              default=get_default_year(), help='year of challenge setting up solution for')
@click.option('-d', '--day', type=click.IntRange(1, 25), required=True, help='day of challenge setting up solution for')
@click.option('--use_cache/--ignore_cache', 'should_use_cache', default=True,
              help='whether to use cached input file [default: true]')
@click.option('--root', 'root_directory', envvar='AOC_ROOT_DIRECTORY',
              type=click.Path(exists=True, file_okay=False, dir_okay=True, writable=True, readable=True, path_type=Path,
                              resolve_path=True), help='root directory of Advent of Code challenges solutions')
@click.option('--session_id', envvar='AOC_SESSION_ID', prompt=True,
              help='session ID to access challenges input [default stored in AOC_SESSION_ID environment variable]')
def command(year: int, day: int, should_use_cache: bool, root_directory: Path, session_id: str):
    """Set up a solution: fetch input and create solution files."""
