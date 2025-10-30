import collections
import functools
import operator
import sys

import p1


def get_answer(input_text: str):
    """Return sum of power of set of cubes, where set is the fewest amounts of cubes colors to be used in that game."""
    games_info = p1.get_games_info(input_text)
    set_cubes_power_sum = 0
    for game in games_info:
        color_to_maximal_amount = collections.defaultdict(int)
        for round_info in game:
            for color, amount in round_info.items():
                color_to_maximal_amount[color] = max(
                    amount, color_to_maximal_amount[color]
                )
        set_cubes_power_sum += functools.reduce(
            operator.mul, color_to_maximal_amount.values()
        )
    return set_cubes_power_sum


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
