from pathlib import Path

import click


@click.command(name='config')
@click.option('--root', 'root_directory', type=consts.ROOT_DIRECTORY_TYPE, prompt=True, prompt_required=False,
              help='root directory of Advent of Code puzzles project')
@click.option('--session-id', help='session ID to access puzzles input')
def command(root_directory: str, session_id: str):
    """Set options."""
    pass
