import subprocess
from pathlib import Path

import bs4
import click

from . import consts, commands_utils
from .commands_utils import get_setting
from .consts import Directories, FileExtensions, HttpMethods


_default_year = commands_utils.get_default_year()


def _parse_result(result: str) -> tuple[str, bool]:
    """
    :param result: result page after submitting an answer
    :return: tuple of (result description, whether the solution was correct or not)
    """
    parsed_result = bs4.BeautifulSoup(result, "html.parser")
    result_paragraph = parsed_result.find("p").text
    first_sentence = result_paragraph.split(".", maxsplit=1)[0] + "."

    right_answer = "That's the right answer!" in first_sentence
    return first_sentence, right_answer


@click.command(name="submit")
@click.option(
    "-y",
    "--year",
    type=click.IntRange(consts.FIRST_AOC_YEAR, _default_year),
    default=_default_year,
    show_default=f"last year: {_default_year}",
    help="year of puzzle setting up solution for",
)
@click.option(
    "-d",
    "--day",
    type=consts.ADVENT_DAYS_RANGE,
    required=True,
    help="day of puzzle to submit",
)
@click.option(
    "-p",
    "--part",
    type=click.Choice(("1", "2")),
    required=True,
    help="puzzle part to submit",
)
@click.option(
    "-n",
    "--no-submit",
    "should_print_only",
    show_default="submit",
    default=False,
    is_flag=True,
    help="should the answer be printed only or submitted too",
)
def command(year: int, day: int, part: int, should_print_only: bool):
    """Submit solution."""
    year = str(year)
    day = str(day).zfill(2)

    root_directory = get_setting(consts.ROOT_DIRECTORY)
    solutions_directory = root_directory / Directories.SOLUTIONS / year / f"d{day}"
    if not solutions_directory.is_dir():
        click.secho(
            "Solution directory does not exist. Run setup command first", fg="red"
        )
        raise click.Abort()

    input_path = (root_directory / Directories.INPUTS / year / day).with_suffix(
        FileExtensions.TEXT
    )
    input_text = input_path.read_text()
    solution_path = (
        root_directory / Directories.SOLUTIONS / year / f"d{day}" / f"p{part}"
    ).with_suffix(FileExtensions.PYTHON)
    answer = _get_answer(input_text, solution_path)
    click.echo(f"Your answer: {answer}")

    if should_print_only:
        return
    result = _get_result_from_website(year, day, part, answer)
    parsed_result = _parse_result(result)
    _print_result(parsed_result)


def _print_result(result: tuple[str, bool]) -> None:
    """
    Print submit result retrieved from the website.
    :param result: result retrieved from the website
    """
    sentence, is_answer_right = result
    color = "green" if is_answer_right else "yellow"
    click.secho(sentence, fg=color)


def _get_result_from_website(year: str, day: str, part: int, answer: str) -> str:
    """
    Submit the answer to the website and return its response to it.
    :param year: year of the puzzle
    :param day: day of the puzzle
    :param part: part of the day's puzzle
    :param answer: puzzle answer to submit
    :return: response from the website
    """
    body = {"level": str(part), "answer": answer}
    day = day.removeprefix(consts.ZERO)
    submit_endpoint = consts.SUBMIT_ENDPOINT_TEMPLATE.substitute(year=year, day=day)
    result = commands_utils.send_aoc_request(HttpMethods.POST, submit_endpoint, body)
    return result


def _get_answer(input_text: str, solution_path: Path) -> str:
    """
    Run the solution module and return the answer.
    :param input_text: input to pass to the solution module
    :param solution_path: path to the Python solution module
    :return: puzzle answer
    :raise: `click.Abort` if an error occurred while running the solution module
    """
    command_arguments = ("python", solution_path, input_text)
    try:
        result = subprocess.run(
            command_arguments, capture_output=True, check=True, text=True
        )
    # If an error occurred in the called solution file, print the exception and abort.
    except subprocess.CalledProcessError as error:
        print(error.stderr)
        raise click.Abort()

    solution = result.stdout.strip()
    return solution
