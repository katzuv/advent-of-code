from pathlib import Path

import click

import consts


@click.command(name='config')
@click.option('--root', 'root_directory', type=consts.ROOT_DIRECTORY_TYPE, prompt=True, prompt_required=False,
              help='root directory of Advent of Code puzzles project')
@click.option('--session-id', help='session ID to access puzzles input')
def command(root_directory: str, session_id: str):
    """Set options."""
    app_data_directory = click.get_app_dir(consts.APP_DATA_DIRECTORY)
    configuration_file = Path(app_data_directory, consts.CONFIGURATION_FILE_NAME)
