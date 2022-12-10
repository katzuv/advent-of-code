from typing import Sequence


class Stack:
    """Class representing a stack of crates."""

    def __init__(self, initial_crates: Sequence[str]):
        """
        Instantiate a stack.
        :param initial_crates: initial crates in the stack
        """
        self._crates = list(initial_crates)
