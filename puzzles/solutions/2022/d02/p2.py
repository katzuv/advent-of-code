import sys

import shapes


DEFEAT = "X"
DRAW = "Y"
WIN = "Z"


def choose_shape(opponent_move: str, outcome: str) -> str:
    """
    :param opponent_move: move the opponent played
    :param outcome: desired outcome of the move
    :return: shape to play for the desired outcome to happen
    """
    if outcome == DEFEAT:
        return shapes.OPPONENT_TO_OUR_SHAPE_DEFEAT[opponent_move]
    if outcome == DRAW:
        for our_shape, opponent_shape in shapes.IDENTICAL_SHAPES.items():
            if opponent_shape == opponent_move:
                return our_shape
    if outcome == WIN:
        for our_shape, opponent_shape in shapes.OUR_TO_OPPONENT_SHAPE_DEFEAT.items():
            if opponent_shape == opponent_move:
                return our_shape


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
