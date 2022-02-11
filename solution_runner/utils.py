import importlib
from pathlib import Path
from types import ModuleType

import consts


def get_module_from_filepath(filepath: Path, directory_relative_to: Path | str = Path.cwd()) -> ModuleType:
    """
    :param filepath: file path to import
    :param directory_relative_to: directory to compute relative path to from `file_path`, default is current directory
    :return: imported module from `file_path`
    """
    if isinstance(directory_relative_to, str):
        directory_relative_to = Path(directory_relative_to)
    module_name = str(filepath.relative_to(directory_relative_to.absolute()).with_suffix(''))
    for path_form, module_form in consts.SEPARATORS_TO_MODULE_NOTATION.items():
        module_name = module_name.replace(path_form, module_form)
    return importlib.import_module(module_name)
