import graphlib
import sys


def get_ordering_rules(ordering_rules: str) -> tuple[int, ...]:
    graph = graphlib.TopologicalSorter()
    for rule in ordering_rules.splitlines():
        dependency, dependant = rule.split("|")
        graph.add(dependant, dependency)

    return tuple(graph.static_order())


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
