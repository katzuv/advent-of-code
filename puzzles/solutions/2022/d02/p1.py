import sys


def get_moves(input_text: str) -> list[tuple[str, str]]:
    """
    :param input_text: puzzle input
    :return: list of (opponent move, our move) couples
    """
    moves = input_text.splitlines()
    return [tuple(move.split()) for move in moves]


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
