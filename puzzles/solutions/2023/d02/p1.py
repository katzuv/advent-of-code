import sys


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


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
