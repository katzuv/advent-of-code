import importlib
from pathlib import Path
from types import ModuleType
from typing import Any

import click
import yaml

import commands.consts
import consts


def get_module_from_filepath(filepath: Path, directory_relative_to: Path | str = Path('.')) -> ModuleType:
    """
    :param filepath: file path to import
    :param directory_relative_to: directory to compute relative path to from `file_path`, default is current directory
    :return: imported module from `file_path`
    """
    module_name = str(filepath.relative_to(directory_relative_to.absolute()).with_suffix(''))
    for path_form, module_form in consts.SEPARATORS_TO_MODULE_NOTATION.items():
        module_name = module_name.replace(path_form, module_form)
    return importlib.import_module(module_name)


def get_setting(key: str) -> Any:
    """
    :param key: key to retrieve its value
    :return: value of `key` which is stored in the configuration file
    """
    configuration_file = commands.consts.APP_DATA_DIRECTORY / commands.consts.CONFIGURATION_FILE_NAME
    try:
        configuration = yaml.safe_load(configuration_file.read_text())
    except FileNotFoundError:
        click.secho("configuration file doesn't exist. Run config command first", fg='red')
        raise

    return configuration[key]
