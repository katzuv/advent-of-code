import sys

# Lowercase item types are numbered 1 through 26, uppercase item types are numbered 27 through 52.
LOWERCASE_ITEM_TYPE_PRIORITY_ASCII_DIFFERENCE = ord("a") - 1
UPPERCASE_ITEM_TYPE_PRIORITY_ASCII_DIFFERENCE = ord("A") - 27


def get_rucksacks_compartments(
    input_text: str,
) -> list[tuple[set, set]]:
    """
    :param input_text: puzzle input
    :return: list of (first compartment set, second compartment set) couples
    """
    return [
        (
            set(rucksack[: len(rucksack) // 2]),
            set(rucksack[len(rucksack) // 2 :]),
        )
        for rucksack in input_text.splitlines()
    ]


def get_shared_item_type(first_compartment: set, second_compartment: set) -> str:
    """
    :param first_compartment: counter of item types in the first compartment
    :param second_compartment: counter of item types in the second compartment
    :return: shared item type between the two compartments
    """
    return (first_compartment & second_compartment).pop()


def get_item_type_priority(item_type: str) -> int:
    """
    :param item_type: item type
    :return: priority of the item type
    """
    difference = (
        LOWERCASE_ITEM_TYPE_PRIORITY_ASCII_DIFFERENCE
        if item_type.islower()
        else UPPERCASE_ITEM_TYPE_PRIORITY_ASCII_DIFFERENCE
    )
    return ord(item_type) - difference


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
