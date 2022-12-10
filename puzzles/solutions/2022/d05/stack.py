from typing import Sequence


class Stack:
    """Class representing a stack of crates."""

    def __init__(self, initial_crates: Sequence[str]):
        """
        Instantiate a stack.
        :param initial_crates: initial crates in the stack
        """
        self._crates = list(initial_crates)

    def remove_crates(self, amount: int) -> list[str]:
        """
        Remove crates from the top of the stack and return a list of them.
        :param amount: amount of crates to remove
        :return: removed crates
        """
        removed = self._crates[-amount:]
        self._crates = self._crates[:-amount]
        return removed
