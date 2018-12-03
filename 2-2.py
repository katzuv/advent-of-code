"""Solution of day 2 part 2."""
from itertools import product
from typing import List


def are_almost_identical(first_id: str, second_id: str) -> bool:
    """
    Return whether two IDs are "almost identical", that is to say they differ by exactly one character at one position.
    :param first_id: first ID to check
    :param second_id: second ID to check
    :return: whether two IDs are "almost identical"
    """
    return sum(char1 != char2 for char1, char2 in zip(first_id, second_id)) == 1


def find_correct_boxes(box_ids: List[str]) -> str:
  """
  :param box_ids: list of the box IDs
  :return: the letters which are common between the two correct box IDs
    for i, first_id in enumerate(box_ids):
        for second_id in box_ids[i:]:
        if are_almost_identical(first_id, second_id):
            return ''.join(
                first_char for first_char, second_char in zip(first_id, second_id) if first_char == second_char).strip()


def strings_from_file(path: str) -> List[str]:
    """
    Return a list of strings which are stored in a file, each string in its own line.
    :param path: path of file with strings
    :return: list of strings from file
    """
    with open(path) as file:
        return [str(line) for line in file]


def main():
    box_ids = strings_from_file('inputs\\2.txt')
    print(set(find_correct_boxes(box_ids)))


if __name__ == '__main__':
    main()
