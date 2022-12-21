import dataclasses


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
