import dataclasses
import math

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

    def move_to_other(self, other: Self) -> None:
        """
        Move this knot, so it will be touching the other knot.
        :param other: other knot to move towards.
        """
        if self.is_touching(other):
            return

        row_distance = self.row - other.row
        column_distance = self.column - other.column

        # If the distance is "far", we want to move the knot, so it will be on the same row/column, but not overlapping,
        #   so the distance to move should be 1.
        # If the distance is "adjacent", it means we want to move diagonally (remember -- the knots are not touching,
        #   otherwise, we would return immediately at the beginning of this method), so the distance to move
        #   stays 1, too.
        # If the distance is 0, no movement should occur, the condition is falsy, so the distance to move stays 0.
        if abs(row_distance) == consts.FAR_DISTANCE:
            row_distance = math.copysign(consts.ADJACENT_DISTANCE, row_distance)
        if abs(column_distance) == consts.FAR_DISTANCE:
            column_distance = math.copysign(consts.ADJACENT_DISTANCE, column_distance)

        self.move((-int(row_distance), -int(column_distance)))
