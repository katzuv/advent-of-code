import copy
import sys

from p1 import get_map_and_start_position, traverse_map, Map, Position


def is_there_a_loop(
    lab_map: Map, start_position: Position, obstacle_position: Position
) -> bool:
    row, column = obstacle_position
    map_with_obstacle = copy.deepcopy(lab_map)
    map_with_obstacle[row][column] = "#"
    try:
        traverse_map(map_with_obstacle, start_position)
    except ValueError:
        return True
    return False


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        print(
            "Warning: No input provided", file=sys.stderr
        )  # Don't crash if no input was passed through command line arguments.
