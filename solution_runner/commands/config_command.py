from pathlib import Path

import click


@click.command(name='config')
@click.option('--root', 'root_directory',
              type=click.Path(exists=True, file_okay=False, dir_okay=True, writable=True, readable=True, path_type=Path,
                              resolve_path=True), help='root directory of Advent of Code puzzles project')
def command(root_directory: Path):
    """Set options."""
    pass
