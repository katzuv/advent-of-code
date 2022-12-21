import dataclasses


@dataclasses.dataclass
class Knot:
    """A knot on a rope which can move."""

    row: int
    column: int
