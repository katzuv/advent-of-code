import subprocess

import bs4
import click

from . import consts, commands_utils
from .commands_utils import get_setting
from .consts import Directories, FileExtensions, HttpMethods


_default_year = commands_utils.get_default_year()


def _get_result(result: str) -> tuple[str, bool]:
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
def command(year: int, day: int, part: int):
    """Submit solution."""
    year = str(year)
    day = str(day)

    root_directory = get_setting(consts.ROOT_DIRECTORY)
    solutions_directory = root_directory / Directories.SOLUTIONS / year / f"d{day}"
    if not solutions_directory.is_dir():
        click.secho(
            "Solution directory does not exist. Run setup command first", fg="red"
        )
        click.Context(command).abort()

    input_path = (root_directory / Directories.INPUTS / year / day).with_suffix(
        FileExtensions.TEXT
    )
    input_text = input_path.read_text()

    part_solution_path = (solutions_directory / f"p{part}").with_suffix(
        FileExtensions.PYTHON
    )
    command_arguments = ("python", part_solution_path, input_text)
    try:
        result = subprocess.run(
            command_arguments, capture_output=True, check=True, text=True
        )
    # If an error occurred in the called solution file, print the exception and abort.
    except subprocess.CalledProcessError as error:
        print(error.stderr)
        raise click.Abort()

    solution = result.stdout.strip()
    body = {"level": str(part), "answer": solution}
    submit_endpoint = consts.SUBMIT_ENDPOINT_TEMPLATE.substitute(year=year, day=day)
    result = commands_utils.send_aoc_request(HttpMethods.POST, submit_endpoint, body)

    sentence, is_answer_right = _get_result(result)
    color = "green" if is_answer_right else "yellow"
    click.secho(sentence, fg=color)
