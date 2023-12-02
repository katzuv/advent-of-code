import sys


MAXIMAL_AMOUNTS = {"red": 12, "green": 13, "blue": 14}


def get_games_info(input_text: str) -> list[[list[dict[str, int]]]]:
    games_info = []
    for line in input_text.splitlines():
        game_info = []
        rounds = line.split(": ")[1].split("; ")
        for round_info in rounds:
            round_color_amounts = {}
            color_amounts = round_info.split(", ")
            for color in color_amounts:
                amount, color = color.split()
                round_color_amounts[color] = int(amount)
            game_info.append(round_color_amounts)
        games_info.append(game_info)

    return games_info


def get_answer(input_text: str) -> int:
    """Return the sum of numbers of possible games."""
    games_info = get_games_info(input_text)
    possible_games_numbers_sum = 0
    for game_number, game in enumerate(games_info, start=1):
        if all(
            amount <= MAXIMAL_AMOUNTS[color]
            for round_info in game
            for color, amount in round_info.items()
        ):
            possible_games_numbers_sum += game_number
    return possible_games_numbers_sum


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
