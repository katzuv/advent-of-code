from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import click


FIRST_AOC_YEAR = 2015
ZERO = '0'
INPUT_URL = 'https://adventofcode.com/{year}/day/{day}/input'
COOKIE = {'session': None}

APP_DATA_DIRECTORY = click.get_app_dir('Advent of Code')
ROOT_DIRECTORY_TYPE = click.Path(file_okay=False, dir_okay=True, writable=True, readable=True, resolve_path=True)


class Directories:
    SOLUTIONS = Path('solutions')
    INPUTS = Path('inputs')


class FileExtensions:
    TEXT = '.txt'
    PYTHON = '.py'


US_EASTERN_TIMEZONE = ZoneInfo('US/Eastern')
AOC_UNLOCK_TIME_TEMPLATE = datetime(year=1, month=12, day=1, hour=0, tzinfo=US_EASTERN_TIMEZONE)
