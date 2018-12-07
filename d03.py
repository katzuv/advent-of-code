import re
from collections import Counter
from itertools import product
from typing import List, Iterable


class Hunk:
    """Class representing a hunk of fabric."""

    def __init__(self, string: str):
        """
        Instantiate a hunk of fabric.
        :param string: string representing the hunk, in the form "{ID} @ {row},{column}: {width}X{height}"
        """
        self.id, self._first_column, self._first_row, width, height = [
            int(s) for s in re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', string).groups()
        ]
        self._one_after_last_column = self._first_column + width
        self._one_after_end_row = self._first_row + height

    def covered_cells(self) -> Iterable[tuple]:
        """
        Return all cells this hunk covers.
        :return: list of covered cells by this hunk
        """
        return product(range(self._first_row, self._one_after_end_row),
                       range(self._first_column, self._one_after_last_column))


def hunks_from_file(path: str = 'inputs\\3.txt') -> List[Hunk]:
    """
    Return a list of hunks which are stored in a file, each hunk claim in its own line.
    :param path: path of file with claims of hunks
    :return: list of hunks from file
    """
    with open(path) as file:
        return [Hunk(line) for line in file]


if __name__ == '__main__':
    hunks = hunks_from_file()
    covered_cells = [cell for hunk in hunks for cell in hunk.covered_cells()]
    covered_cells_amounts = Counter(covered_cells).values()
    duplicates = sum(count > 1 for count in covered_cells_amounts)
    print(f"Amount of duplicates: {duplicates}")
