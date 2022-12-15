import consts
from directory import Directory
from file import File


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


def handle_ls_command(directory: Directory, command: str) -> None:
    """
    Add contents to the given directory, according to the given `ls` command output.
    :param command: `ls` command output
    :param directory: directory to add contents to
    """
    contents = command.splitlines()[1:]
    for content in contents:
        if content.startswith(consts.DIRECTORY_SYMBOL):
            directory_name = content.split()[1]
            directory.add_subdirectory(Directory(directory_name, directory))
        else:
            size, filename = content.split()
            directory.add_file(File(filename, int(size)))
