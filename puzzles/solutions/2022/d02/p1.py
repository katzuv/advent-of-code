import sys

import consts


def get_moves(input_text: str) -> tuple[tuple[str, str], ...]:
    """
    :param input_text: puzzle input
    :return: list of (opponent move, our move) pairs
    """
    input_text = input_text.translate(
        str.maketrans(consts.IDENTICAL_SHAPES)
    )  # Replace opponent shapes with generic shapes.
    moves = input_text.splitlines()
    return tuple(tuple(move.split()) for move in moves)


def calculate_move_score(move: tuple[str, str]) -> int:
    """
    :param move: pair of (opponent move, our move)
    :return: total score of the move
    """
    score = 0
    opponent_move, our_move = move
    if consts.WINNING_MOVES[our_move] == opponent_move:
        score += consts.WIN_SCORE
    elif opponent_move == our_move:
        score += consts.DRAW_SCORE

    score += consts.SHAPE_TO_SCORE[our_move]
    return score


def get_answer(input_text: str):
    """Return the total score if everything goes exactly according to our strategy guide."""
    moves = get_moves(input_text)
    total_score = sum(calculate_move_score(move) for move in moves)
    return total_score


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
