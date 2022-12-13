from typing import Sequence, Iterable


class Stack:
    """Class representing a stack of crates."""

    def __init__(self, initial_crates: Sequence[str]):
        """
        Instantiate a stack.
        :param initial_crates: initial crates in the stack
        """
        self._crates = list(initial_crates)

    def __str__(self) -> str:
        """
        :return: a string representation of the crates in the stack
        """
        return " ".join(self._crates)

    def remove_crates(self, amount: int) -> Iterable[str]:
        """
        Remove crates from the top of the stack and return a list of them.
        :param amount: amount of crates to remove
        :return: removed crates
        """
        removed = self._crates[-amount:]
        self._crates = self._crates[:-amount]
        return reversed(removed)

    def add_crates(self, crates: Iterable[str]):
        """
        Add crates to the stack.
        :param crates: crates to add to the stack
        """
        self._crates.extend(crates)

    @property
    def top(self) -> str:
        """
        :return: crate at the top of the stack
        """
        return self._crates[-1]
