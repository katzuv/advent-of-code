from zoneinfo import ZoneInfo


FIRST_AOC_YEAR = 2015
ZERO = '0'


class FileExtensions:
    TEXT = '.txt'
    PYTHON = '.py'


US_EASTERN_TIMEZONE = ZoneInfo('US/Eastern')
AOC_UNLOCK_TIME_TEMPLATE = datetime.datetime(year=1, month=12, day=1, hour=0, tzinfo=US_EASTERN_TIMEZONE)
