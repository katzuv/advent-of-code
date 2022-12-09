"""Various constants used for Rock Paper Scissors shapes and other data about them."""


OUR_ROCK = "X"
OUR_PAPER = "Y"
OUR_SCISSORS = "Z"
OPPONENT_ROCK = "A"
OPPONENT_PAPER = "B"
OPPONENT_SCISSORS = "C"

OUR_TO_OPPONENT_SHAPE_DEFEAT = {
    OUR_ROCK: OPPONENT_SCISSORS,
    OUR_PAPER: OPPONENT_ROCK,
    OUR_SCISSORS: OPPONENT_PAPER,
}
