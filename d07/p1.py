from typing import List, Tuple


def couples_from_file(path: str = '..\\inputs\\7.txt') -> List[Tuple[str, str]]:
    """
    :return: list of steps-couples from file
    """
    with open(path) as file:
        return [(line[5], line[36]) for line in file]


def steps_to_after(couples):  # List[Tuple[str, str]]): -> Dict[str: List[str]]:
    edges = {node: [] for node in {couple[0] for couple in couples} | {couple[1] for couple in couples}}
    for dependency, step in couples:
        edges[dependency].append(step)
    return edges


def steps_to_their_dependencies(couples):  # List[Tuple[str, str]]): -> Dict[str: List[str]]:
    edges = {node: [] for node in {couple[0] for couple in couples} | {couple[1] for couple in couples}}
    for dependency, step in couples:
        edges[step].append(dependency)
    return edges


def topological_sorting(couples):  # Dict[str: List[str]]): -> List[str]:
    """
    :param couples: couples of (dependency of step: step)
    :return: topological sorted list of nodes of a graph
    """
    sorted_elements = []
    steps_to_dependencies = steps_to_their_dependencies(couples)
    steps_to_next = steps_to_after(couples)
    no_incoming_edges = {node for node in steps_to_dependencies if not steps_to_dependencies[node]}
    possible_steps = []
    first_time = True
    while no_incoming_edges:
        current_step = min(no_incoming_edges)
        no_incoming_edges.remove(current_step)
        sorted_elements.append(current_step)
        for dependencies in steps_to_dependencies.values():
            try:
                dependencies.remove(current_step)
            except ValueError:
                pass

        if first_time:
            possible_steps.extend(list(no_incoming_edges))
            first_time = False
        for dependent_step in steps_to_next[current_step]:
            if not steps_to_dependencies[dependent_step]:
                possible_steps.append(dependent_step)
        if not possible_steps:
            return ''.join(sorted_elements)
        next_step = min(possible_steps)
        possible_steps.remove(next_step)
        no_incoming_edges.add(next_step)


def main():
    print(f'Part one solution: {topological_sorting(couples_from_file())}')


if __name__ == '__main__':
    main()
