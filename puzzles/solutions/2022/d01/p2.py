import sys

import p1


def get_answer(input_text: str):
    """Return the total calories carried by the top three Elves carrying the most calories."""
    inventories = p1.get_inventories(input_text)
    sums = p1.get_calories_sums(inventories)

    descending_calories = sorted(sums, reverse=True)
    return sum(descending_calories[:3])


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
