import consts
from directory import Directory


def get_next_directory(current_directory: Directory, command: str) -> Directory:
    """
    :param current_directory: current directory
    :param command: `cd` command to parse
    :return: `cd` command object
    """
    destination = command.split()[1]
    if destination == consts.PARENT_DIRECTORY_SYMBOL:
        return current_directory.parent
    for subdirectory in current_directory.subdirectories:
        if subdirectory.name == destination:
            return subdirectory
