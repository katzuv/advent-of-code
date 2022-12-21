import dataclasses

from typing import Self

import consts


@dataclasses.dataclass
class Knot:
    """A knot on a rope which can move."""

    row: int
    column: int

    def move(self, step: tuple[int, int]) -> None:
        """
        Move the knot by the given step.
        :param step: pair of (row, column) movement
        """
        x, y = step
        self.row += x
        self.column += y

    def is_touching(self, other: Self) -> bool:
        """
        :param other: other knot
        :return: whether this knot and the other knot are touching
        """
        return (
            abs(self.row - other.row) < consts.FAR_DISTANCE
            and abs(self.column - other.column) < consts.FAR_DISTANCE
        )
