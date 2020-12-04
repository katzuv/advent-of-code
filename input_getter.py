from pathlib import Path

import requests

URL = 'https://adventofcode.com/{year}/day/{day_number}/input'
COOKIE = dict(
    session='53616c7465645f5f405c809e0f85ce95631c200e0fe9b1651e31982e553be0d2d03af5a96bd8625b5cd8c11167112e9e')
HTTP_OK_CODE = 200

INPUT_DIRECTORY_NAME = Path('inputs')
TXT_SUFFIX = '.txt'

DAY_DIRECTORY_PATH = 'd{day_number}'


def get_input(year: str, day_number: str) -> str:
    url = URL.format(year=year, day_number=day_number)
    r = requests.get(url, cookies=COOKIE)
    if r.status_code != 200:
        print(url)
        raise ConnectionError(f'Something went wrong. Response: {r.text}')
    return r.text


def get_year_input() -> str:
    year_input = input('Enter year (2020 is default): ')
    if year_input == '':
        year_input = '2020'
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
