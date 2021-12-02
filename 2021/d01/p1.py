from pathlib import Path
from typing import Iterator

INPUT_FILE_PATH = Path('..', 'inputs', '1.txt')


def get_measurements_from_input(input_text: str) -> list[int]:
    """
    :param input_text: input test to process
    :return: split measurements from the input
    """
    return list(map(int, input_text.splitlines()))


def get_depth_measurements_increases(measurements: Iterator[int]) -> int:
    """
    :param measurements: measurements to parse
    :return: count of the number of times a depth measurement increases
    """
    couples = zip(measurements[:-1], measurements[1:])
    return sum(couple[1] > couple[0] for couple in couples)


def main():
    input_text = INPUT_FILE_PATH.read_text()
    measurements = get_measurements_from_input(input_text)

    depth_measurements_increases = get_depth_measurements_increases(measurements)
    print(f'Amount of measurements which are larger than the previous measurement: {depth_measurements_increases}')


if __name__ == '__main__':
    main()
