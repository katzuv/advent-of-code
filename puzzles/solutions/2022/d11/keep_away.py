from monkey import Monkey


class KeepAway:
    """Class managing the monkeys' Keep Away game."""

    def __init__(self, monkeys: list[Monkey]):
        self._monkeys = monkeys
