from typing import List


def have_n_letters(identifier, n):
    return any(list(identifier).count(char) == n for char in identifier)


def checksum(ids):
    contain_double = 0
    contain_triple = 0
    for identifier in ids:
        if have_n_letters(identifier, 2):
            contain_double += 1
        if have_n_letters(identifier, 3):
            contain_triple += 1
    return contain_double * contain_triple


def strings_from_file(path: str) -> List[str]:
    """
    Return a list of floats which are stored in a file, each number in its own line.
    :param path: path of file with floats
    :return: list of numbers from file
    """
    with open(path) as file:
        return [str(line) for line in file]
