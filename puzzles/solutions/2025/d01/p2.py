import sys

from p1 import get_turns


def get_answer(input_text: str):
    turns = get_turns(input_text)

    current_turn = 50

    visits_at_zero = 0

    # Because of how division works with negative numbers, we need to split the logic between going left and right.
    for turn in turns:
        # If everything's positive, we can use regular floor division.
        if turn > 0:
            times_at_zero = (current_turn + turn) // 100

        else:
            # Take the additive inverse for simpler math.
            steps = -turn
            dist_to_first_zero = 100 if current_turn == 0 else current_turn
            # If we have "enough" steps to hit the first zero...
            if steps >= dist_to_first_zero:
                # We visited a zero for the first time.
                visits_at_zero += 1
                # Count how many zeros our steps can hit after the first zero.
                times_at_zero = (steps - dist_to_first_zero) // 100
            # Not enough steps to hit the first zero.
            else:
                times_at_zero = 0

        # Fortunately this works fine for negative numbers as well, so no need to split.
        current_turn = (current_turn + turn) % 100
        visits_at_zero += times_at_zero

    return visits_at_zero


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        print(
            "Warning: No input provided", file=sys.stderr
        )  # Don't crash if no input was passed through command line arguments.
