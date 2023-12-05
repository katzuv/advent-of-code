import sys

from input_parser import Coordinate


def _reconstruct_path(
    node_to_parent: dict[Coordinate:Coordinate], end: Coordinate
) -> list[Coordinate]:
    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = node_to_parent[current]
    return path


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
