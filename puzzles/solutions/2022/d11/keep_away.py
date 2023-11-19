from monkey import Monkey


class KeepAway:
    """Class managing the monkeys' Keep Away game."""

    _RELIEF_WORRY_REDUCTION_FACTOR = 3
    _ROUNDS_AMOUNT = 20

    def __init__(self, monkeys: list[Monkey]):
        self._monkeys = monkeys

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
