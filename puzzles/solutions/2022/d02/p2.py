import sys

import p1
import shapes


def choose_shape(opponent_move: str, outcome: str) -> str:
    """
    :param opponent_move: move the opponent played
    :param outcome: desired outcome of the move
    :return: shape to play for the desired outcome to happen
    """
    mapping = shapes.OUTCOME_TO_MAPPING[outcome]
    for our_move in mapping:
        if mapping[our_move] == opponent_move:
            return our_move


def generate_moves(
    moves_outcomes: tuple[tuple[str, str]]
) -> tuple[tuple[str, str], ...]:
    """
    :param moves_outcomes: list of (opponent move, desired outcome) pairs
    :return: list of (opponent move, desired move for desired outcome to happen) pairs
    """
    return tuple(
        (opponent_move, choose_shape(opponent_move, outcome))
        for opponent_move, outcome in moves_outcomes
    )


def get_answer(input_text: str):
    """Return the total score if everything goes exactly according to our actual strategy guide."""
    moves_outcomes = p1.get_moves(input_text)
    moves = generate_moves(moves_outcomes)
    total_score = sum(p1.calculate_move_score(move) for move in moves)
    return total_score


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
