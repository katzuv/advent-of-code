import sys


def get_trees_map(input_text: str) -> tuple[tuple[int, ...], ...]:
    """
    :param input_text: puzzle input
    :return: tuple of tuples representing the map of the tress
    """
    return tuple(tuple(map(int, row)) for row in input_text.splitlines())


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
