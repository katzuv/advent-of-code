import functools
import sys

GROUP_SIZE = 3


def get_group_rucksacks(input_text: str) -> list[list[str]]:
    """
    :param input_text: puzzle input
    :return: list of combined rucksacks in a group
    """
    rucksacks = input_text.splitlines()
    groups = []
    for rucksack_number in range(0, len(rucksacks), GROUP_SIZE):
        group_rucksacks = rucksacks[rucksack_number : rucksack_number + GROUP_SIZE]
        groups.append(group_rucksacks)
    return groups


def get_group_badge(group_rucksacks: list[str]) -> str:
    """
    :param group_rucksacks: list of rucksacks of the group
    :return: group badge, which is the item type which is common between all rucksacks
    """
    group_rucksacks = map(set, group_rucksacks)
    return tuple(functools.reduce(set.intersection, group_rucksacks))[0]


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
