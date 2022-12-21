import itertools
import sys
from typing import Sequence
import p1


def get_adjacent_trees(
    trees_map: Sequence[Sequence[int]],
    map_length: int,
    map_width: int,
    tree_row: int,
    tree_column: int,
) -> tuple[tuple[int, ...], ...]:
    """
    Return adjacent trees of the tree which is on the given coordinates, without the tree itself,
    and starting with the tree closest to the given tree outwards.
    :param trees_map: map of the trees
    :param map_length: length of the map
    :param map_width: width of the map
    :param tree_row: row number the tree is on
    :param tree_column: column number the tree is on
    :return: adjacent trees of the tree which is on the given coordinates
    """
    top, bottom, left, right = p1.get_adjacent_trees(
        trees_map, map_length, map_width, tree_row, tree_column
    )
    return tuple(reversed(top)), bottom, tuple(reversed(left)), right


def get_tree_scenic_score(
    tree_height: int, adjacent_trees: Sequence[Sequence[int]]
) -> int:
    """
    :param tree_height: height of the tree
    :param adjacent_trees: sequences of adjacent trees
    :return: the tree's scenic score
    """
    scenic_score = 1
    for trees_run in adjacent_trees:
        trees_until_blocking_tree = len(
            tuple(itertools.takewhile(lambda tree: tree < tree_height, trees_run))
        )
        # Blocking trees are seen, and because `takewhile` stops before the blocking tree, we add a tree
        # to the viewing distance, but only if we haven't already reached the end of the line.
        if trees_until_blocking_tree < len(trees_run):
            trees_until_blocking_tree += 1
        scenic_score *= trees_until_blocking_tree
    return scenic_score


def get_answer(input_text: str):
    """Return the highest scenic score possible for any tree."""
    trees_map = p1.get_trees_map(input_text)
    map_length = len(trees_map)
    map_width = len(trees_map[0])

    highest_scenic_score = 0
    for row, column in itertools.product(range(map_length), range(map_width)):
        tree_height = trees_map[row][column]
        adjacent_trees = get_adjacent_trees(
            trees_map, map_length, map_width, row, column
        )
        scenic_score = get_tree_scenic_score(tree_height, adjacent_trees)
        highest_scenic_score = max(highest_scenic_score, scenic_score)

    return highest_scenic_score


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.