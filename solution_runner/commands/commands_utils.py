from enum import Enum
from typing import Any

import click
import yaml

from . import consts


class PathType(Enum):
    FILE = 1
    DIRECTORY = 2


def get_setting(key: str) -> Any:
    """
    :param key: key to retrieve its value
    :return: value of `key` which is stored in the configuration file
    """
    configuration_file = consts.APP_DATA_DIRECTORY / consts.CONFIGURATION_FILE_NAME
    try:
        configuration = yaml.safe_load(configuration_file.read_text())
    except FileNotFoundError:
        click.secho("configuration file doesn't exist. Run config command first", fg='red')
        raise

    return configuration[key]
