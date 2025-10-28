import graphlib
import sys


def get_ordering_rules(ordering_rules: str) -> tuple[int, ...]:
    graph = graphlib.TopologicalSorter()
    for rule in ordering_rules.splitlines():
        dependency, dependant = rule.split("|")
        graph.add(dependant, dependency)

    return tuple(graph.static_order())


def is_update_in_right_order(order: tuple[int, ...], update: list[str]) -> bool:
    previous_page_number_index = -1
    for page_number in update:
        current_page_number_index = order.index(page_number)
        if current_page_number_index < previous_page_number_index:
            return False
        previous_page_number_index = current_page_number_index
    return True


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
