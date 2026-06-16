import copy
import itertools
import multiprocessing
import sys

from p1 import get_map_and_start_position, traverse_map, Map, Position


def is_there_a_loop(inputs: tuple[Map, Position, Position]) -> bool:
    lab_map, start_position, obstacle_position = inputs

    row, column = obstacle_position
    map_with_obstacle = copy.deepcopy(lab_map)
    map_with_obstacle[row][column] = "#"
    try:
        traverse_map(map_with_obstacle, start_position)
    except ValueError:
        return True
    return False


def get_answer(input_text: str) -> int:
    lab_map, start_position = get_map_and_start_position(input_text)
    original_traversed_map = traverse_map(lab_map, start_position)
    map_coordinates = tuple(
        itertools.product(range(len(lab_map)), range(len(lab_map[0])))
    )

    path = [
        (row, column)
        for (row, column) in map_coordinates
        if original_traversed_map[row][column] == "X"
    ]
    path.remove(start_position)  # Can't put an obstacle on the guard's start position.
    # print(len(path))

    with multiprocessing.Pool(multiprocessing.cpu_count() - 1) as pool:
        return sum(
            pool.map(
                is_there_a_loop,
                zip(
                    itertools.repeat(lab_map),
                    itertools.repeat(start_position),
                    path,
                ),
            )
        )


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        print(
            "Warning: No input provided", file=sys.stderr
        )  # Don't crash if no input was passed through command line arguments.
