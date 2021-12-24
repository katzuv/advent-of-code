from pathlib import Path

import click


@click.command(name='config')
@click.option('--root', 'root_directory',
              type=click.Path(exists=True, file_okay=False, dir_okay=True, writable=True, readable=True, path_type=Path,
                              resolve_path=True), help='root directory of Advent of Code puzzles project')
@click.option('--session-id', help='session ID to access puzzles input')
def command(root_directory: Path, session_id: str):
    """Set options."""
    pass
