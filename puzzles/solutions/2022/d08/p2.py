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
    tree_height: int, adjacent_trees: Sequence[Sequence[int, ...], ...]
) -> int:
    """
    :param tree_height: height of the tree
    :param adjacent_trees: sequences of adjacent trees
    :return: the tree's scenic score
    """
    scenic_score = 1
    for trees_run in adjacent_trees:
        trees_until_blocking_tree = len(
            tuple(itertools.takewhile(lambda tree: tree <= tree_height, trees_run))
        )
        scenic_score *= trees_until_blocking_tree
    return scenic_score


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
