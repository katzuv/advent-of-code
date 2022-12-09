from pathlib import Path
from typing import Any

import click
import yaml

from . import consts


@click.command(name="config")
@click.option(
    "--root",
    "root_directory",
    type=consts.ROOT_DIRECTORY_TYPE,
    prompt=True,
    prompt_required=False,
    help="root directory of Advent of Code puzzles project",
)
@click.option(
    "--session-id",
    prompt=True,
    prompt_required=False,
    hide_input=True,
    help="session ID to access puzzles input",
)
def command(root_directory: str, session_id: str):
    """Set options."""
    app_data_directory = click.get_app_dir(consts.APP_DATA_DIRECTORY)
    configuration_file = Path(app_data_directory, consts.CONFIGURATION_FILE_NAME)
    try:
        # Use an empty dictionary if no actual configuration is in the configuration file.
        configuration = yaml.safe_load(configuration_file.read_text()) or {}
    except FileNotFoundError:
        Path(app_data_directory).mkdir(exist_ok=True)
        configuration_file.touch()
        configuration = {}
    initial_configuration = configuration.copy()

    root_directory = _configure_root_directory(configuration, root_directory)
    root_directory = Path(root_directory)
    root_directory.mkdir(exist_ok=True)

    _configure_session_id(configuration, session_id)

    if configuration != initial_configuration:
        configuration_file.write_text(yaml.dump(configuration))


def _configure_root_directory(
    configuration: dict[str, Any], root_directory: str | None
) -> str:
    """
    Edit the root directory configuration if needed.
    :param configuration: current configuration
    :param root_directory: root directory passed by the user, `None` if wasn't passed
    :return: root directory after configuration if needed
    """
    if root_directory is not None:
        configuration[consts.ROOT_DIRECTORY] = root_directory
    elif consts.ROOT_DIRECTORY not in configuration:
        configuration[consts.ROOT_DIRECTORY] = click.prompt(
            "Enter path for Advent of Code project root directory",
            type=consts.ROOT_DIRECTORY_TYPE,
        )
    return configuration[consts.ROOT_DIRECTORY]


def _configure_session_id(configuration: dict[str, Any], session_id: str | None):
    """
    Configure the session ID if needed.
    :param configuration: current configuration
    :param session_id: session ID passed by the user, `None` if wasn't passed
    """
    if session_id is not None:
        configuration[consts.SESSION_ID] = session_id
    elif consts.SESSION_ID not in configuration:
        configuration[consts.SESSION_ID] = click.prompt(
            "Enter session ID to download input files (available in AoC website cookies)",
            hide_input=True,
        )
