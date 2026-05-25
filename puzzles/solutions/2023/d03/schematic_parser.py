import itertools
import string
from typing import Iterable


class SchematicParser:
    """Class that parsers the engine schematic."""

    def __init__(self, engine_schematic: str):
        self._schematic = engine_schematic.splitlines()
        self._schematic_length = len(self._schematic)
        self._schematic_width = len(self._schematic[0])

        self._numbers = []
        self._gears_positions = []

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

    def find_part_numbers(self) -> list[int]:
        current_digits = []
        is_adjacent_to_symbol = False

        for row, column in itertools.product(
            range(self._schematic_length), range(self._schematic_width)
        ):
            character = self._schematic[row][column]
            if character.isdigit():
                current_digits.append(character)
                is_adjacent_to_symbol |= self._is_character_adjacent_to_character(
                    row, column, string.digits + ".", False
                )
            # Avoid edge case where there is a part number at the end of one line and another on the
            # start of the following line -- we want to treat them as two different part numbers.
            if not character.isdigit() or column == self._schematic_width - 1:
                if is_adjacent_to_symbol:
                    self._add_number(row, column, current_digits)
                current_digits = []
                is_adjacent_to_symbol = False

        return [number for number, digits_positions in self._numbers]

    def find_gears(self):
        for row, column in itertools.product(
            range(self._schematic_length), range(self._schematic_width)
        ):
            if self._schematic[row][column] == "*":
                self._gears_positions.append((row, column))

    @staticmethod
    def _is_number_adjacent(
        position: tuple[int, int], digits_positions: Iterable[tuple[int, int]]
    ) -> bool:
        position_row, position_column = position
        return any(
            abs(row - position_row) <= 1 and abs(column - position_column) <= 1
            for row, column in digits_positions
        )

    def calculate_gear_ratios_sum(self):
        gear_ratios_sum = 0
        for gear_position in self._gears_positions:
            adjacent_numbers = [
                number
                for number, digits_positions in self._numbers
                if self._is_number_adjacent(gear_position, digits_positions)
            ]
            if len(adjacent_numbers) == 2:
                gear_ratio = adjacent_numbers[0] * adjacent_numbers[1]
                gear_ratios_sum += gear_ratio
        return gear_ratios_sum
