from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import click


FIRST_AOC_YEAR = 2015
DECEMBER = 12
ZERO = '0'
INPUT_URL = 'https://adventofcode.com/{year}/day/{day}/input'
SESSION = 'session'

APP_DATA_DIRECTORY = click.get_app_dir('Advent of Code')
CONFIGURATION_FILE_NAME = Path('configuration.yaml')
ROOT_DIRECTORY_TYPE = click.Path(file_okay=False, dir_okay=True, writable=True, readable=True, resolve_path=True)
ROOT_DIRECTORY = 'root directory'
SESSION_ID = 'session ID'
SOLUTION_FILE_CONTENT = Path(Path(__file__).parent, 'solution_template.py').read_text()


class Directories:
    SOLUTIONS = Path('solutions')
    INPUTS = Path('inputs')


class FileExtensions:
    TEXT = '.txt'
    PYTHON = '.py'


US_EASTERN_TIMEZONE = ZoneInfo('US/Eastern')
AOC_UNLOCK_TIME_TEMPLATE = datetime(year=1, month=12, day=1, hour=0, tzinfo=US_EASTERN_TIMEZONE)
