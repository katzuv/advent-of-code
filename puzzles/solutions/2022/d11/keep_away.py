from typing import Callable, Iterable

from monkey import Monkey


class KeepAway:
    """Class managing the monkeys' Keep Away game."""

    _RELIEF_WORRY_REDUCTION_FACTOR = 3

    def __init__(
        self,
        monkeys: list[Monkey],
        rounds_amount: int,
        worry_level_modifier: Callable[[int, Iterable[Monkey]], int],
    ):
        self._monkeys = monkeys
        self._rounds_amount = rounds_amount
        self._worry_level_modifier = worry_level_modifier

    def _handle_item(self, item: int, monkey: Monkey) -> None:
        """
        Handle a single item -- calculate its worry level and determine the monkey to which the item will be thrown.
        :param item: item to handle
        :param monkey: monkey who plays the current turn
        """
        worry_level = item
        worry_level = monkey.worry_function(worry_level)
        worry_level //= self._RELIEF_WORRY_REDUCTION_FACTOR
        monkey_number_to_throw_item_to = (
            monkey.true_test_result_monkey_number
            if worry_level % monkey.test_divisor == 0
            else monkey.false_test_result_monkey_number
        )
        monkey.throw(self._monkeys[monkey_number_to_throw_item_to], worry_level)

    def _run_turn(self, monkey: Monkey) -> None:
        """
        Run a turn.
        :param monkey: monkey who plays the current turn
        """
        items = monkey.items[:]
        for item in items:
            self._handle_item(item, monkey)
        monkey.empty_items()

    def run(self) -> None:
        """Run the Keep Away game."""
        for _ in range(self._rounds_amount):
            for monkey in self._monkeys:
                self._run_turn(monkey)

    def get_monkey_business_level(self) -> int:
        """
        :return: monkey business level, which is the product of the inspected items amount of the two most active
        monkeys in the game.
        """
        two_most_active_monkeys = sorted(
            self._monkeys, key=lambda monkey: monkey.inspected_items_amount
        )[-2:]
        monkey_business = (
            two_most_active_monkeys[0].inspected_items_amount
            * two_most_active_monkeys[1].inspected_items_amount
        )
        return monkey_business
