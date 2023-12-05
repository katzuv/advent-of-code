import sys

import input_parser
from input_parser import Coordinate
import queue


def shortest_path(
    start: Coordinate, graph: dict[Coordinate, list[Coordinate]]
) -> list[Coordinate]:
    """
    :param start: start node
    :param graph: mapping of positions to climbable neighbors
    :return: shortest path between the start and end position
    """
    state_queue = queue.Queue()
    state_queue.put(start)
    visited = {start}
    node_to_parent = {start: None}
    while not state_queue.empty():
        current = state_queue.get()
        if current.is_end:
            return _reconstruct_path(node_to_parent, current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                state_queue.put(neighbor)
                visited.add(neighbor)
                node_to_parent[neighbor] = current


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
    """Return the fewest steps required to move from the start to the end position."""
    start, graph = input_parser.get_graph(input_text)
    path = shortest_path(start, graph)
    steps = len(path) - 1
    return steps


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
