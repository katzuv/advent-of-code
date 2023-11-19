import dataclasses
from typing import Callable


@dataclasses.dataclass
class Monkey:
    """Class representing a monkey playing Keep Away."""

    items: list[int]
    worry_function: Callable[[int], int]
    test_divisor: int
    true_test_result_monkey_number: int
    false_test_result_monkey_number: int
    inspected_items_amount: int = 0
