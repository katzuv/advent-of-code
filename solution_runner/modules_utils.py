"""Filepaths and modules utils."""
from pathlib import Path

import consts


def convert_filepath_to_relative_module(filepath: Path, directory_relative_to: Path | str = Path('.')) -> str:
    """
    :param filepath: file path to convert to module
    :param directory_relative_to: directory to compute relative path to from `file_path`, default is current directory
    :return: module name in relative terms to `file_path`
    """
    module_name = str(filepath.relative_to(directory_relative_to))
    for path_form, module_form in consts.SEPARATORS_TO_MODULE_NOTATION.values():
        module_name = module_name.replace(path_form, module_form)
    return module_name
