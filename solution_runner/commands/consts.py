import string
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import click


FIRST_AOC_YEAR = 2015
DECEMBER = 12
ADVENT_DAYS_RANGE = click.IntRange(1, 25)
ZERO = '0'
BASE_URL = 'https://adventofcode.com/'
INPUT_ENDPOINT_TEMPLATE = string.Template('/$year/day/$day/input')
SUBMIT_ENDPOINT_TEMPLATE = string.Template('/$year/day/$day/answer')
SESSION = 'session'
# Requested by Advent of Code owner to help track requests.
USER_AGENT_HEADER = {'User-Agent': 'AoC.CLI.katzuv'}

APP_DATA_DIRECTORY = click.get_app_dir('Advent of Code')
CONFIGURATION_FILE_NAME = Path('configuration.yaml')
ROOT_DIRECTORY_TYPE = click.Path(file_okay=False, dir_okay=True, writable=True, readable=True, resolve_path=True)
ROOT_DIRECTORY = 'root directory'
SOLUTION_PARTS = ('p1', 'p2')
SESSION_ID = 'session ID'
SOLUTION_FILE_CONTENT = Path(Path(__file__).parent, 'solution_template.py').read_text()


class Directories:
    SOLUTIONS = Path('solutions')
    INPUTS = Path('inputs')


class FileExtensions:
    TEXT = '.txt'
    PYTHON = '.py'


class HttpMethods:
    GET = 'GET'
    POST = 'POST'


US_EASTERN_TIMEZONE = ZoneInfo('US/Eastern')
AOC_UNLOCK_TIME_TEMPLATE = datetime(year=1, month=12, day=1, hour=0, tzinfo=US_EASTERN_TIMEZONE)
