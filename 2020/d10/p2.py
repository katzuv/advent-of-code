import functools
from pprint import pprint
import random
from typing import Union

from frozendict import frozendict
from p1 import get_adapters_from_input, INPUT_FILE_PATH


class Node:
    def __init__(self, name: str, parent=None):
        self.name = name
        self.parent = parent
        self.children = []

    def __repr__(self):
        if self.parent is not None:
            return f'{self.__class__.__name__}({self.name}, {self.parent})'
        return f'{self.__class__.__name__}({self.name})'

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value
        if value is not None:
            value.children.append(self)

    @property
    def descendants(self) -> list:
        result = self.children[:]
        for child in self.children:
            result.extend(child.descendants)
        return result


def get_next_available_adapters(adapter_joltage: int, adapters: tuple[int]) -> tuple[int]:
    return tuple(adapter for adapter in adapters if 0 < adapter - adapter_joltage <= 3)


leaves = 0


@functools.cache
def construct_dict(adapter: int, available_adapters: tuple[int]) -> frozendict:
    next_adapters = get_next_available_adapters(adapter, available_adapters)
    result = {}
    for next_adapter in next_adapters:
        result[next_adapter] = construct_dict(next_adapter, available_adapters[1:])
    return frozendict(result)


i = 0


@functools.cache
def count_leaves(tree: Union[dict, frozendict]) -> int:
    global i
    print(i)
    i += 1
    total = 0
    if len(tree) == 0:
        total += 1
    for child in tree.values():
        total += count_leaves(child)
    return total


@functools.cache
def construct_tree(adapter: Node, available_adapters: tuple[int]):
    adapter_joltage = int(adapter.name)
    next_adapters = get_next_available_adapters(adapter_joltage, available_adapters)
    for next_adapter in next_adapters:
        node = Node(str(next_adapter), parent=adapter)
        remaining_adapters = available_adapters[1:]
        construct_tree(node, remaining_adapters)


def print_tree(node: Node, indent=0):
    for child in node.children:
        print(' ' * indent, child)
        print_tree(child, indent + 1)


def main():
    input_text = INPUT_FILE_PATH.read_text()
    adapters = get_adapters_from_input(input_text)
    adapters.sort()

    tree = construct_dict(0, tuple(adapters))
    print(construct_dict.cache_info())
    # pprint(tree)
    print(count_leaves(tree))
    print(count_leaves.cache_info())
    # print(construct_tree.cache_info())
    # print_tree(root)
    # leaves = len([node for node in root.descendants if len(node.children) == 0])
    # print(f'Total number of arrangements: {leaves}')


if __name__ == '__main__':
    main()
