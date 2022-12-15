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

    def add_subdirectory(self, subdirectory: Self) -> None:
        """
        :param subdirectory: subdirectory to add to the directory
        """
        self._subdirectories.append(subdirectory)

    @property
    def files(self) -> tuple[File, ...]:
        """
        :return: files in the directory
        """
        return tuple(self._files)

    @property
    def subdirectories(self) -> tuple[Self, ...]:
        """
        :return: subdirectories of the directory
        """
        return tuple(self._subdirectories)
