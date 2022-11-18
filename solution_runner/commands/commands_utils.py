import urllib.parse
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any

import click
import requests
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
        click.secho(
            "configuration file doesn't exist. Run config command first", fg="red"
        )
        raise

    return configuration[key]


def check_path_exists(path: Path, command: click.Command, path_type: str = None):
    """
    Abort if path doesn't exist.
    :param path: path to check
    :param command: command to be passed to`click.Context` if aborting is needed
    :param path_type: optional "dir" or "file". If not passed, only check for existence. If passed, check for type.
    """
    match path_type:
        case None:
            if not path.exists():
                click.secho(f"{path} doesn't exist", fg="red")
        case "dir":
            if not path.is_dir():
                click.secho(
                    f"Directory at {path} doesn't exist or isn't a directory", fg="red"
                )
        case "file":
            if not path.is_file():
                click.secho(f"File at {path} doesn't exist or isn't a file", fg="red")
        case _:
            return  # If everything is OK, exit the function before aborting.
    click.Context(command).abort()


def send_aoc_request(method, endpoint: str, payload=None) -> str:
    """
    Send a request to Advent of Code's website and return the textual response.
    :param method: method of the request
    :param endpoint: endpoint to append to the base URL
    :param payload: optional payload to attach to the request
    :return: text content of the response
    """
    if payload is None:
        payload = {}
    session_id = get_setting(consts.SESSION_ID)
    cookies = {consts.SESSION: session_id}
    url = urllib.parse.urljoin(consts.BASE_URL, endpoint)

    request = requests.request(
        method, url, headers=consts.USER_AGENT_HEADER, cookies=cookies, data=payload
    )
    request.raise_for_status()
    return request.text


def get_default_year() -> int:
    """
    :return: default year which is the current year if it's December, last year otherwise
    """
    today = datetime.today()
    current_year = today.year
    if today.month == consts.DECEMBER:
        return current_year
    return current_year - 1
