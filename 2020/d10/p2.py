from collections import defaultdict
from pprint import pprint

from p1 import get_adapters_from_input, INPUT_FILE_PATH


class Node:
    def __init__(self, name: int):
        self.name = name
        self.parents = []
        self.children = []

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name})'

    @property
    def descendants(self) -> list:
        result = self.children[:]
        for child in self.children:
            result.extend(child.descendants)
        return result

    def __eq__(self, other):
        return self.name == other.name


def get_next_available_adapters(adapter_joltage: int, adapters: list[int]) -> list[int]:
    return [adapter for adapter in adapters if 0 < adapter - adapter_joltage <= 3]


def print_tree(node: Node, indent=0):
    for child in node.children:
        print(' ' * indent, child)
        print_tree(child, indent + 1)


def populate_adapters(adapters: list[int]):
    result = defaultdict(list)
    for adapter_joltage in adapters:
        for next_adapter in get_next_available_adapters(adapter_joltage, adapters):
            result[adapter_joltage].append(next_adapter)
    return result


def get_node(next_adapter: int, nodes: list[Node]):
    for node in nodes:
        if node.name == next_adapter:
            return node
    raise ValueError(f'No adapter with {next_adapter} joltage found')


def get_arrangements_amount(adapter: int, adapters_to_next: dict[int, list[int]],
                            adapter_to_amount: dict[int, int]) -> int:
    if len(adapters_to_next[adapter]) == 0:
        return 1
    result = 0
    for next_adapter in adapters_to_next[adapter]:
        amount = adapter_to_amount[next_adapter]
        result += amount * get_arrangements_amount(next_adapter, adapters_to_next, adapter_to_amount)
    return result


def count_adapters(adapters: dict[int, list[int]]) -> dict[int, int]:
    histogram = defaultdict(int)
    all_adapters = []
    for adapters_lists in adapters.values():
        all_adapters.extend(adapters_lists)

    for adapter in all_adapters:
        histogram[adapter] += 1

    return histogram


def main():
    input_text = INPUT_FILE_PATH.read_text()
    adapters = get_adapters_from_input(input_text)
    adapters.sort()

    adapters_to_next = populate_adapters(adapters)
    adapter_to_amount = count_adapters(adapters_to_next)
    # print(adapter_to_amount)
    # pprint(adapters_to_next)

    total = 1

    arrangements = get_arrangements_amount(0, adapters_to_next, adapter_to_amount)
    # print(f'Total number of arrangements: {arrangements}')


if __name__ == '__main__':
    main()
