import sys

import shapes


def get_moves(input_text: str) -> list[tuple[str, str]]:
    """
    :param input_text: puzzle input
    :return: list of (opponent move, our move) couples
    """
    moves = input_text.splitlines()
    return [tuple(move.split()) for move in moves]


def calculate_move_score(move: tuple[str, str]) -> int:
    """
    :param move: couple of (opponent move, our move) couples
    :return: total score of the move
    """
    score = 0
    opponent_move, our_move = move
    if shapes.OUR_TO_OPPONENT_SHAPE_DEFEAT[our_move] == opponent_move:
        score += 6
    elif shapes.IDENTICAL_SHAPES[our_move] == opponent_move:
        score += 3

    score += shapes.SHAPE_TO_SCORE[our_move]
    return score


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
