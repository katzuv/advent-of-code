from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


FIRST_AOC_YEAR = 2015
ZERO = '0'
INPUT_URL = 'https://adventofcode.com/{year}/day/{day}/input'
COOKIE = {'session': None}

CONFIGURATION_KEY_TO_PARAMETERS = {
    # Explanation, type to use to check the value against, stored type in configuration file, whether to hide input.
    'root_directory': ('root directory of Advent of Code project', Path, str, False),
    'session_id': ('session ID to download input files (can be accessed from AoC website cookies', str, str, True)
}


class Directories:
    SOLUTIONS = Path('solutions')
    INPUTS = Path('inputs')


class FileExtensions:
    TEXT = '.txt'
    PYTHON = '.py'


US_EASTERN_TIMEZONE = ZoneInfo('US/Eastern')
AOC_UNLOCK_TIME_TEMPLATE = datetime(year=1, month=12, day=1, hour=0, tzinfo=US_EASTERN_TIMEZONE)
