from pathlib import Path

import click
import yaml

import consts


@click.command(name='config')
@click.option('--root', 'root_directory',
              type=click.Path(exists=True, file_okay=False, dir_okay=True, writable=True, readable=True, path_type=Path,
                              resolve_path=True), help='root directory of Advent of Code puzzles project')
@click.option('--session-id', help='session ID to access puzzles input')
def command(root_directory: Path, session_id: str):
    """Set options."""
    app_data_directory = Path(click.get_app_dir('Advent of Code'))
    configuration_file = Path(app_data_directory, consts.CONFIGURATION_FILE_NAME)
    try:
        configuration = yaml.safe_load(configuration_file.read_text()) or {}
        configuration_changed = False
    except FileNotFoundError:
        app_data_directory.mkdir(exist_ok=True)
        configuration_file.touch()
        configuration = {}
        configuration_changed = True

    for key, (explanation, check_type, stored_type, hide_input) in consts.CONFIGURATION_KEY_TO_PARAMETERS.items():
        if key in configuration:
            continue

        configuration_changed = True
        value = click.prompt(f'Enter {explanation}', hide_input=hide_input, type=check_type)
        value = stored_type(value)
        configuration[key] = value

    if configuration_changed:
        configuration_file.write_text(yaml.dump(configuration))


command()
