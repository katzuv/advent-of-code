from pathlib import Path

INPUT_FILE_PATH = Path('..', 'inputs', '1.txt')


def get_measurements_from_input(input_text: str) -> list:
    """
    :param input_text: input test to process
    :return: split measurements from the input
    """
    return list(map(int, input_text.splitlines()))
