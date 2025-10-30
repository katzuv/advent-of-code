import copy
import itertools
import sys

Map = list[list[str]]

Position = tuple[int, int]


def get_map_and_start_position(input_text: str) -> tuple[Map, Position]:
    lab_map = [list(row) for row in input_text.splitlines()]
    for row in range(len(lab_map)):
        try:
            column = lab_map[row].index("^")
        except ValueError:
            continue
        position = row, column
        lab_map[row][column] = "."
        break
    return lab_map, position


def traverse_map(lab_map: Map, start_position: Position) -> Map:
    row, column = start_position
    new_map = copy.deepcopy(lab_map)

    directions = itertools.cycle(((-1, 0), (0, 1), (1, 0), (0, -1)))
    steps_taken = []

    direction = next(directions)
    while True:
        new_map[row][column] = "X"
        step = ((row, column), direction)
        if step in steps_taken:
            raise ValueError("Loop detected!")
        steps_taken.append(step)

        next_row, next_column = (row + direction[0], column + direction[1])

        try:
            if lab_map[next_row][next_column] == "#":
                direction = next(directions)
                continue
        except IndexError:
            break

        row, column = next_row, next_column
    return new_map


def get_answer(input_text: str) -> int:
    lab_map, start_position = get_map_and_start_position(input_text)
    new_map = traverse_map(lab_map, start_position)
    return sum(row.count("X") for row in new_map)


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        print(
            "Warning: No input provided", file=sys.stderr
        )  # Don't crash if no input was passed through command line arguments.
