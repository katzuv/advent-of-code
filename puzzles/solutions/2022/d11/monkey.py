import dataclasses
from typing import Callable, Self


@dataclasses.dataclass
class Monkey:
    """Class representing a monkey playing Keep Away."""

    items: list[int]
    worry_function: Callable[[int], int]
    test_divisor: int
    true_test_result_monkey_number: int
    false_test_result_monkey_number: int
    inspected_items_amount: int = 0

    def throw(self, other: Self, item_to_throw: int) -> None:
        """
        Throw the given item to another monkey.

        This method also increments the items inspected amount (every inspected item is eventually thrown).
        :param other: other monkey to throw item to
        :param item_to_throw: item to throw
        """
        other.items.append(item_to_throw)
        self.inspected_items_amount += 1
