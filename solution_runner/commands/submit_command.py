import subprocess

import click

from . import consts
from .commands_utils import get_setting
from .consts import Directories, FileExtensions, HttpMethods
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

    root_directory = get_setting(consts.ROOT_DIRECTORY)
    solutions_directory = root_directory / Directories.SOLUTIONS / year / f"d{day}"
    if not solutions_directory.is_dir():
        click.secho("Solution directory does not exist. Run setup command first", fg='red')
        click.Context(command).abort()

    input_path = (root_directory / Directories.INPUTS / year / day).with_suffix(FileExtensions.TEXT)
    input_text = input_path.read_text()

    part_solution_path = (solutions_directory / f"p{part}").with_suffix(FileExtensions.PYTHON)
    command_arguments = ("python", part_solution_path, input_text)
    try:
        result = subprocess.run(command_arguments, capture_output=True, check=True, text=True)
    # If an error occurred in the called solution file, print the exception and abort.
    except subprocess.CalledProcessError as error:
        print(error.stderr)
        raise click.Abort()

    solution = result.stdout.strip()
