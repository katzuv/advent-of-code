"""Solution of day 1 part 2."""

from typing import Sequence


def first_duplicate(sequence: Sequence[float]) -> float:
    """
    Return the first number repeated in a sequence which every number in it becomes the sum of itself and the number
    before it.

    Note: it is assumed a duplicate number will be found, including a case where it might be needed to repeat the
    sequence many times before a duplicate is found.

    :param sequence: sequence to be checked
    :return: first value repeated in a sequence
    """
    frequencies = [0]
    while True:
        for line in sequence:
            current_sum = frequencies[-1] + int(line)
            frequencies.append(current_sum)
            if current_sum in frequencies[:-1]:
                return current_sum


def numbers_from_file(path: str) -> list:
    """
    Return a list of floats which are stored in a file, each number in its own line.
    :param path: path of file with floats
    :return: list of numbers from file
    """
    with open(path) as file:
        return [float(line) for line in file]


def main():
    frequencies = numbers_from_file('input.txt')
    print(frequencies)
    print(first_duplicate(frequencies))


if __name__ == '__main__':
    main()
