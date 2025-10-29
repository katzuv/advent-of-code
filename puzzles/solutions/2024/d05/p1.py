import collections
import sys

Graph = dict[str, set[str]]


def get_ordering_rules(ordering_rules: str) -> Graph:
    graph = collections.defaultdict(set)
    for rule in ordering_rules.splitlines():
        dependency, dependant = rule.split("|")
        graph[dependant].add(dependency)

    return graph


def is_update_in_right_order(order: tuple[int, ...], update: list[str]) -> bool:
    previous_page_number_index = -1
    for page_number in update:
        current_page_number_index = order.index(page_number)
        if current_page_number_index < previous_page_number_index:
            return False
        previous_page_number_index = current_page_number_index
    return True


def get_answer(input_text: str) -> int:
    ordering_rules, updates = input_text.split("\n\n")
    order = get_ordering_rules(ordering_rules)
    updates = [update.split(",") for update in updates.splitlines()]

    return sum(
        int(update[len(update) // 2])  # Middle page number.
        for update in updates
        if is_update_in_right_order(order, update)
    )


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
