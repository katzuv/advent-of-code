from monkey import Monkey


class KeepAway:
    """Class managing the monkeys' Keep Away game."""

    _RELIEF_WORRY_REDUCTION_FACTOR = 3

    def __init__(self, monkeys: list[Monkey]):
        self._monkeys = monkeys
