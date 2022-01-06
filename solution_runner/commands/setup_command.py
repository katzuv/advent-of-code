from datetime import datetime
from pathlib import Path

import click
import requests

from . import consts
from .consts import Directories, FileExtensions
from .defaults_and_choices import get_default_year


_default_year = get_default_year()


@click.command(name='setup')
@click.option('-y', '--year', type=click.IntRange(consts.FIRST_AOC_YEAR, _default_year), default=_default_year,
              show_default=f'last year: {_default_year}', help='year of puzzle setting up solution for')
@click.option('-d', '--day', type=click.IntRange(1, 25), required=True, help='day of puzzle setting up solution for')
@click.option('--use_cache/--ignore_cache', 'should_use_cache', default=True, show_default='true',
              help='whether to use cached input file')
def command(year: int, day: int, should_use_cache: bool):
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


def _ask_user_to_mkdir(directory: Path, name: str = None):
    """
    Ask the user whether to create the given directory and abort if negative.

    Should be use for directories which do not exist.
    :param directory: directory to ask about
    :param name: name of the directory to ask the user about, given directory name is default
    """
    if directory.is_dir():
        return

    if name is None:
        name = directory.name
    if click.confirm(f"{name} directory doesn't exist, do you want to create it?", prompt_suffix='', default=True,
                     show_default=True, abort=True):
        directory.mkdir()


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


def _download_input(year: str, day: str, input_file: Path, session_id: str):
    """
    Download the puzzle's input and write it to a file.
    :param year: year of the puzzle
    :param day: day of the puzzle
    :param input_file: input file path
    :param session_id: session ID to download input from website
    """
    day = day.lstrip(consts.ZERO)
    url = consts.INPUT_URL.format(year=year, day=day)
    cookie = {'session': session_id}

    request = requests.get(url, cookies=cookie)
    request.raise_for_status()

    input_text = request.text
    input_file.write_text(input_text)
