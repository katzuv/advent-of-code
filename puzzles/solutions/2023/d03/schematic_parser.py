import itertools
from typing import Iterable


class SchematicParser:
    """Class that parsers the engine schematic."""

    def __init__(self, engine_schematic: str):
        self._schematic = engine_schematic.splitlines()
        self._schematic_length = len(self._schematic)
        self._schematic_width = len(self._schematic[0])

        self._numbers = []

    def _is_character_adjacent_to_character(
        self,
        character_row: int,
        character_column: int,
        characters: Iterable[str],
        should_match: bool,
    ) -> bool:
        """
        :param character_row: row of the checked character
        :param character_column: column of the checked character
        :param characters: characters to check against
        :param should_match: should the character be adjacent one of the given characters or not
        :return: whether the character is (not) adjacent to the given characters
        """
        upper_row = max(0, character_row - 1)
        lower_row = min(self._schematic_length - 1, character_row + 1)
        left_column = max(0, character_column - 1)
        right_column = min(self._schematic_width - 1, character_column + 1)

        neighbors = list(
            itertools.product(
                range(upper_row, lower_row + 1), range(left_column, right_column + 1)
            )
        )
        neighbors.remove((character_row, character_column))
        for row, column in neighbors:
            character = self._schematic[row][column]
            if (character in characters) == should_match:
                return True

        return False

    def _add_number(self, row: int, column: int, digits: list[str]) -> None:
        if not digits:
            return

        number = int("".join(digits))
        first_column = column - len(digits)
        positions = tuple(zip(itertools.repeat(row), range(first_column, column)))
        self._numbers.append((number, positions))
