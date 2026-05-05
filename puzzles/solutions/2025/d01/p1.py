import sys


def get_turns(input_text: str) -> list[int]:
    turns = []
    for turn in input_text.splitlines():
        direction = turn[0]
        steps = int(turn[1:])
        if direction == "L":
            steps *= -1
        turns.append(steps)
    return turns


def get_answer(input_text: str):
    turns = get_turns(input_text)


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        print(
            "Warning: No input provided", file=sys.stderr
        )  # Don't crash if no input was passed through command line arguments.
