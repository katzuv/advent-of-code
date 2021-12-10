from datetime import datetime

import click

import consts
from defaults_and_choices import get_default_year


@click.command(name='setup')
@click.option('-y', '--year', type=click.IntRange(consts.FIRST_AOC_YEAR, get_default_year()),
              default=get_default_year(), help='year of puzzle setting up solution for')
@click.option('-d', '--day', type=click.IntRange(1, 25), required=True, help='day of puzzle setting up solution for')
@click.option('--use_cache/--ignore_cache', 'should_use_cache', default=True,
              help='whether to use cached input file [default: true]')
@click.option('--root', 'root_directory', required=True, envvar='AOC_ROOT_DIRECTORY', prompt=True,
              type=click.Path(exists=True, file_okay=False, dir_okay=True, writable=True, readable=True, path_type=Path,
                              resolve_path=True), help='root directory of Advent of Code puzzles solutions')
@click.option('--session_id', envvar='AOC_SESSION_ID', prompt=True,
              help='session ID to access puzzles input [default stored in AOC_SESSION_ID environment variable]')
def command(year: int, day: int, should_use_cache: bool, root_directory: Path, session_id: str):
    """Set up a solution: fetch input and create solution files."""


def _abort_if_puzzle_locked(year: int, day: int):
    """
    Check if the puzzle at the given time wasn't unlocked yet, and abort if true.
    :param year: year of the puzzle
    :param day: day of the puzzle
    """
    puzzle_unlock_time = consts.AOC_UNLOCK_TIME_TEMPLATE.replace(year=year, day=day)
    now = datetime.now(tz=consts.US_EASTERN_TIMEZONE)
    if puzzle_unlock_time > now:
        click.secho(f"{year}'s day {day} puzzle wasn't unlocked yet.", fg='red')
        click.Context(command).abort()


def _abort_input_file_already_exists(year: str, day: str):
    """
    Abort the script because the input file and notify the user.
    :param year: year of the puzzle
    :param day: day of the puzzle
    """
    day = day.lstrip(consts.ZERO)  # Remove leading zeros for prettier printing.
    click.secho(f"Input file for {year}'s day {day} puzzle already exists.", fg='red')
    click.Context(command).abort()


def _create_files(year_solutions_directory: Path, day: str):
    """
    Create challenge directory and files.
    :param year_solutions_directory: challenges solution files of the relevant year
    :param day: day of the challenge
    """
    solutions_directory = year_solutions_directory / day
    solutions_directory.mkdir()
    for part in ('1', '2'):
        filepath = (solutions_directory / part).with_suffix(FileExtensions.PYTHON)
        filepath.touch()
