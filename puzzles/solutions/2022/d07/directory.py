from typing import Self


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