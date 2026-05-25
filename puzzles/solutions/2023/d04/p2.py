import sys


import p1


def get_answer(input_text: str) -> int:
    """Return the amount of cards we end up with."""
    cards = [p1.get_card_from_line(line) for line in input_text.splitlines()]

    card_to_matching_numbers = {}
    for card in cards:
        matching_numbers_amount = len(card.winning_numbers & card.chosen_numbers)
        cards_copies_numbers = range(
            card.number + 1, card.number + matching_numbers_amount + 1
        )
        card_to_matching_numbers[card.number] = cards_copies_numbers

    card_to_amount = {card.number: 1 for card in cards}

    for card, matching_numbers in card_to_matching_numbers.items():
        for matching_number in matching_numbers:
            card_to_amount[matching_number] += card_to_amount[card]

    return sum(card_to_amount.values())


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
