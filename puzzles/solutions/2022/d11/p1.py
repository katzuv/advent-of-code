import sys
from monkey import Monkey
from monkey_creator import create_monkey
from keep_away import KeepAway


def create_monkeys(input_text: str) -> list[Monkey]:
    """
    :param input_text: puzzle input
    :return: list of monkeys
    """
    monkeys = []
    for monkey_attributes in input_text.split("\n\n"):
        monkey_attributes = tuple(map(str.strip, monkey_attributes.splitlines()))
        monkey = create_monkey(monkey_attributes[1:])
        monkeys.append(monkey)
    return monkeys


def get_answer(input_text: str):
    """Get the monkey business level at the end of the Keep Away game."""
    monkeys = create_monkeys(input_text)
    game = KeepAway(monkeys)
    game.run()
    return game.get_monkey_business_level()


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
