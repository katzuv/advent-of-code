from collections import defaultdict
from pathlib import Path

from anytree import Node

COM = 'COM'


class OrbitCountChecksumCalculator:
    def __init__(self, orbits: dict[str, list[str]]):
        self._orbits = orbits
        self.com = Node(COM)
        self._construct_tree(self.com)

    def _construct_tree(self, orbited: Node):
        for orbiter in self._orbits.get(orbited.name, []):
            node = Node(orbiter, parent=orbited)
            self._construct_tree(node)

    def get_node(self, name: str) -> Node:
        for node in self.com.descendants:
            if node.name == name:
                return node
        raise ValueError(f'Node {name} not found')


def get_orbits_from_input() -> dict[str: list[str]]:
    input_file = Path('..', 'inputs', '6.txt')
    couples = input_file.read_text().splitlines()
    orbits = defaultdict(list)
    for couple in couples:
        orbited, orbiter = couple.split(')')
        orbits[orbited].append(orbiter)
    return orbits


def main():
    orbits = get_orbits_from_input()

    calc = OrbitCountChecksumCalculator(orbits)
    total_orbits = sum(str(node).count(calc.com.separator) - 1 for node in calc.com.descendants)
    print(f'Total amount of direct and indirect orbits: {total_orbits}')


if __name__ == '__main__':
    main()
