import collections
import sys


Card = collections.namedtuple("Card", ("number", "winning_numbers", "chosen_numbers"))


def get_card_from_line(card_line: str) -> Card:
    card_number, numbers_lists = card_line.split(": ")
    card_number = card_number.split()[1]

    winning_numbers, chosen_numbers = numbers_lists.split(" | ")
    winning_numbers = set(winning_numbers.split())
    chosen_numbers = set(chosen_numbers.split())

    return Card(card_number, winning_numbers, chosen_numbers)


def calculate_card_points(card: Card) -> int:
    amount_of_card_winning_numbers = len(card.winning_numbers & card.chosen_numbers)
    if amount_of_card_winning_numbers == 0:
        return 0
    return 2 ** (amount_of_card_winning_numbers - 1)


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
