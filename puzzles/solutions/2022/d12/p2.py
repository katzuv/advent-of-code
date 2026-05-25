import sys

import input_parser
import p1


def get_answer(input_text: str):
    """Return the fewest steps required to move from any "a" elevation position to the end position."""
    _, graph = input_parser.get_graph(input_text)
    lowest_elevation = ord("a")
    start = [position for position in graph if position.elevation == lowest_elevation]
    path = p1.shortest_path(start, graph)
    steps = len(path) - 1
    return steps


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
