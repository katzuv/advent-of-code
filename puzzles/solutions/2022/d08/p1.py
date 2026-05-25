import itertools
import sys
from typing import Sequence


MAX_TREE_HEIGHT = 10


def get_trees_map(input_text: str) -> tuple[tuple[int, ...], ...]:
    """
    :param input_text: puzzle input
    :return: tuple of tuples representing the map of the tress
    """
    return tuple(tuple(map(int, row)) for row in input_text.splitlines())


def get_adjacent_trees(
    trees_map: Sequence[Sequence[int]],
    map_length: int,
    map_width: int,
    tree_row: int,
    tree_column: int,
) -> tuple[tuple[int, ...], ...]:
    """
    :param trees_map: map of the trees
    :param map_length: length of the map
    :param map_width: width of the map
    :param tree_row: row number the tree is on
    :param tree_column: column number the tree is on
    :return: adjacent trees of the tree which is on the given coordinates, without the tree itself
    """
    column = [trees_map[row][tree_column] for row in range(map_length)]
    top = tuple(column[:tree_row])
    bottom = tuple(column[tree_row + 1 :])
    row = [trees_map[tree_row][column] for column in range(map_width)]
    left = tuple(row[:tree_column])
    right = tuple(row[tree_column + 1 :])
    return top, bottom, left, right


def is_tree_visible(
    tree_height: int, adjacent_trees: tuple[tuple[int, ...], ...]
) -> bool:
    return any(
        tree_height
        > max(
            current_adjacent_trees or (MAX_TREE_HEIGHT,)
        )  # `max` raises a `ValueError` if given an empty iterator.
        for current_adjacent_trees in adjacent_trees
    )


def get_edge_trees_amount(map_length: int, map_width: int) -> int:
    """
    :param map_length: length of the map
    :param map_width: width of the map
    :return: amount of trees on the edges of the map
    """
    return map_length * 2 + (map_width - 2) * 2


def get_answer(input_text: str):
    trees_map = get_trees_map(input_text)
    map_length = len(trees_map)
    map_width = len(trees_map[0])

    visible_tress = 0
    for row, column in itertools.product(
        range(1, map_length - 1), range(1, map_width - 1)
    ):
        adjacent_trees = get_adjacent_trees(
            trees_map, map_length, map_width, row, column
        )
        tree_height = trees_map[row][column]
        if is_tree_visible(tree_height, adjacent_trees):
            visible_tress += 1
    return visible_tress + get_edge_trees_amount(map_length, map_width)


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
