from typing import Self

from file import File


class Directory:
    """A directory which can store files and subdirectories."""

    def __init__(self, name: str, parent: Self = None):
        """
        Instantiate a directory.
        :param name: name of the directory
        :param parent: parent directory, if exists
        """
        self.name = name
        self.parent = parent
        self._files = []
        self._subdirectories = []

    def add_file(self, file: File) -> None:
        """
        :param file: file to add to the directory
        """
        self._files.append(file)
