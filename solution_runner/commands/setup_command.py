import errno
import shutil
from datetime import datetime
from pathlib import Path

import click
import git
import github

from . import consts, commands_utils
from .consts import Directories, FileExtensions, HttpMethods

_default_year = commands_utils.get_default_year()


@click.command(name="setup")
@click.option(
    "-y",
    "--year",
    type=click.IntRange(consts.FIRST_AOC_YEAR, _default_year),
    default=_default_year,
    show_default=f"last year: {_default_year}",
    help="year of puzzle to set up solution for",
)
@click.option(
    "-d",
    "--day",
    type=consts.ADVENT_DAYS_RANGE,
    required=True,
    help="day of puzzle to set up solution for",
)
@click.option(
    "--use-cache/--ignore-cache",
    "should_use_cache",
    default=True,
    show_default="true",
    help="whether to use cached input file",
)
def command(year: int, day: int, should_use_cache: bool):
    """Set up a solution: fetch input and create solution files."""
    _abort_if_puzzle_locked(year, day)

    year = str(year)
    day = str(day).zfill(2)  # Add a leading zero for single digit numbers.

    try:
        root_directory = commands_utils.get_setting(consts.ROOT_DIRECTORY)
    except FileNotFoundError:
        raise click.Abort()
    inputs_directory = root_directory / Directories.INPUTS
    _ask_user_to_mkdir(inputs_directory, "input files")

    year_inputs_directory = inputs_directory / year
    _ask_user_to_mkdir(year_inputs_directory, f"{year} input files")
    input_file = (year_inputs_directory / day).with_suffix(FileExtensions.TEXT)

    if (
        should_use_cache
        and input_file.exists()
        and input_file.stat().st_size
        > 0  # Abort only if the file exists, and it is not empty.
    ):
        _abort_input_file_already_exists(year, day)

    _download_input(year, day, input_file)

    solutions_directory = root_directory / Directories.SOLUTIONS
    _ask_user_to_mkdir(solutions_directory, "solution files")

    year_solutions_directory = solutions_directory / year
    _ask_user_to_mkdir(year_solutions_directory, f"{year} solution files")
    _create_files(year_solutions_directory, day)

    branch_name = f"solve/{year_solutions_directory.name}-{day}"
    _initialize_git_branch(branch_name, year_solutions_directory, day)
    _open_pull_request(branch_name, year, day)


def _abort_if_puzzle_locked(year: int, day: int):
    """
    Check if the puzzle at the given time wasn't unlocked yet, and abort if true.
    :param year: year of the puzzle
    :param day: day of the puzzle
    """
    puzzle_unlock_time = consts.AOC_UNLOCK_TIME_TEMPLATE.replace(year=year, day=day)
    now = datetime.now(tz=consts.US_EASTERN_TIMEZONE)
    if puzzle_unlock_time > now:
        click.secho(f"{year}'s day {day} puzzle wasn't unlocked yet.", fg="red")
        raise click.Abort()


def _ask_user_to_mkdir(directory: Path, name: str = None):
    """
    Ask the user whether to create the given directory and abort if negative.

    Should be used for directories which do not exist.
    :param directory: directory to ask about
    :param name: name of the directory to ask the user about, given directory name is default
    """
    if directory.is_dir():
        return

    if name is None:
        name = directory.name
    if click.confirm(
        f"{name} directory doesn't exist, do you want to create it?",
        prompt_suffix="",
        default=True,
        show_default=True,
        abort=True,
    ):
        directory.mkdir()


def _abort_input_file_already_exists(year: str, day: str):
    """
    Abort the script because the input file and notify the user.
    :param year: year of the puzzle
    :param day: day of the puzzle
    """
    day = day.lstrip(consts.ZERO)  # Remove leading zeros for prettier printing.
    click.secho(f"Input file for {year}'s day {day} puzzle already exists.", fg="red")
    raise click.Abort()


def _create_files(year_solutions_directory: Path, day: str):
    """
    Create challenge directory and files.
    :param year_solutions_directory: challenges solution files of the relevant year
    :param day: day of the challenge
    """
    solutions_directory = year_solutions_directory / f"d{day}"
    try:
        solutions_directory.mkdir()
    except FileExistsError as error:
        if error.errno == errno.EEXIST:
            return  # If solution directory already exists, don't create new solution files.
        raise
    for part in consts.SOLUTION_PARTS:
        filepath = (solutions_directory / part).with_suffix(FileExtensions.PYTHON)
        shutil.copy(consts.SOLUTION_FILE_TEMPLATE_PATH, filepath)


def _download_input(year: str, day: str, input_file: Path):
    """
    Download the puzzle's input and write it to a file.
    :param year: year of the puzzle
    :param day: day of the puzzle
    :param input_file: input file path
    """
    day = day.lstrip(consts.ZERO)
    endpoint = consts.INPUT_ENDPOINT_TEMPLATE.substitute(year=year, day=day)
    input_text = commands_utils.send_aoc_request(HttpMethods.GET, endpoint)
    input_file.write_text(input_text)


def _initialize_git_branch(branch_name: str, year_solutions_directory: Path, day: str):
    repo = git.Repo(".")
    repo.git.checkout(b=branch_name)

    repo.index.add(year_solutions_directory / f"d{day}" / "p1.py")
    repo.index.commit("Create solution file for part 1")

    repo.git.push("origin", "--set-upstream", branch_name)


def _open_pull_request(branch_name: str, year: str, day: str):
    day = day.lstrip(consts.ZERO)
    auth = github.Auth.Token(commands_utils.get_setting(consts.GITHUB_AUTH_TOKEN))
    repo_name = (
        git.Repo()
        .remote("origin")
        .url.split("https://github.com/")[1]
        .removesuffix(".git")
    )
    repo = github.Github(auth=auth).get_repo(repo_name)
    repo.create_pull(
        base="main", head=branch_name, title=f"Solve {year} day {day}", draft=True
    )
