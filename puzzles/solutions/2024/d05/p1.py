import collections
import sys

Graph = dict[str, set[str]]


def get_ordering_rules(ordering_rules: str) -> Graph:
    graph = collections.defaultdict(set)
    for rule in ordering_rules.splitlines():
        dependency, dependant = rule.split("|")
        graph[dependant].add(dependency)

    return graph


def is_update_in_right_order(update: list[str], graph: Graph) -> bool:
    done_pages = set()
    for i, page_number in enumerate(update):
        left_pages = set(update[i + 1 :])
        next_pages_dependencies = left_pages & graph[page_number]
        if not (next_pages_dependencies <= done_pages):
            return False
        done_pages.add(page_number)
    return True


def get_answer(input_text: str) -> int:
    ordering_rules, updates = input_text.split("\n\n")
    order = get_ordering_rules(ordering_rules)
    updates = [update.split(",") for update in updates.splitlines()]

    return sum(
        int(update[len(update) // 2])  # Middle page number.
        for update in updates
        if is_update_in_right_order(update, order)
    )


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
