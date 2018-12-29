"""Solution of day 2 part 1."""


from typing import List


def have_n_letters(box_id: str, n: int) -> bool:
    """
    Return whether an ID has n of any character.
    :param box_id: the ID to check
    :param n: exact amount of characters
    :return: whether an ID has n of any character
    """
    return any(box_id.count(char) == n for char in box_id)


def checksum(box_ids: List[str]) -> int:
    """
    Return the checksum of list of box IDs.
    :param box_ids: list of box IDs
    :return: checksum of the list of box IDs
    """
    contain_double = 0
    contain_triple = 0
    for identifier in box_ids:
        if have_n_letters(identifier, 2):
            contain_double += 1
        if have_n_letters(identifier, 3):
            contain_triple += 1
    return contain_double * contain_triple


def strings_from_file(path: str) -> List[str]:
    """
    Return a list of strings which are stored in a file, each string in its own line.
    :param path: path of file with strings
    :return: list of strings from file
    """
    with open(path) as file:
        return [str(line) for line in file]


def main():
    box_ids = strings_from_file('..\\inputs\\2.txt')
    print(checksum(box_ids))


if __name__ == '__main__':
    main()
