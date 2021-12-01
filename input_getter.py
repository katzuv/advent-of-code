from datetime import datetime
from pathlib import Path

import requests

from session_id import SESSION_ID

URL = 'https://adventofcode.com/{year}/day/{day_number}/input'
COOKIE = {'session': SESSION_ID}
HTTP_OK_CODE = 200

INPUT_DIRECTORY_NAME = Path('inputs')
TXT_SUFFIX = '.txt'

DAY_DIRECTORY_PATH = 'd{day_number}'


def get_input(year: str, day_number: str) -> str:
    url = URL.format(year=year, day_number=day_number)
    request = requests.get(url, cookies=COOKIE)
    request.raise_for_status()
    return request.text


def get_year_input() -> str:
    current_year = str(datetime.today().year)
    year_input = input(f'Enter year ({current_year} is default): ')
    if year_input == '':
        year_input = current_year
    return year_input


def get_day_input() -> str:
    day_number_input = input('Enter day number: ')
    return day_number_input


def write_input_file(year: str, day: str, input_text: str):
    input_directory_path = Path(year, INPUT_DIRECTORY_NAME)
    input_directory_path.mkdir(parents=True, exist_ok=True)
    input_file = (input_directory_path / day).with_suffix(TXT_SUFFIX)
    input_file.write_text(input_text)


def create_solutions_directory(year: str, day: str):
    padded_day_number = day.rjust(2, '0')
    solution_directory_path = Path(year, DAY_DIRECTORY_PATH.format(day_number=padded_day_number))
    if solution_directory_path.exists():
        return

    solution_directory_path.mkdir()
    for part in (1, 2):
        part_solution_path = solution_directory_path / f'p{part}.py'
        part_solution_path.touch()


def main():
    year_input = get_year_input()
    day_input = get_day_input()

    input_text = get_input(year_input, day_input)
    write_input_file(year_input, day_input, input_text)

    create_solutions_directory(year_input, day_input)


if __name__ == '__main__':
    main()
