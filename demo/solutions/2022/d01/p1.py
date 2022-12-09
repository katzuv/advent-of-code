import sys


def get_inventories(input_text: str) -> list[list[int]]:
    """
    :param input_text: puzzle input
    :return: list of elves' inventories
    """
    inventories = input_text.split("\n\n")  # Inventories are split by a blank line.
    return [[int(item) for item in inventory.splitlines()] for inventory in inventories]


def get_calories_sums(inventories: list[list[int]]):
    """
    :param: inventories: list of inventories
    :return: list containing the sum of each inventory
    """
    return list(map(sum, inventories))


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    print(get_answer(sys.argv[1]))
