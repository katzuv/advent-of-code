from collections import namedtuple
from itertools import product, tee
from typing import Tuple, List, Iterable

Coordinate = namedtuple('Coordinate', ['x', 'y'])


class Rectangle:
    def __init__(self, min_x, max_x, min_y, max_y):
        self._min_x = min_x
        self._max_x = max_x
        self._min_y = min_y
        self._max_y = max_y

    def all_coordinates(self):
        return [Coordinate(x, y)
                for x, y in product(range(self._min_x, self._max_x + 1), range(self._min_y, self._max_y + 1))]

    def __contains__(self, coordinate: Coordinate):
        return self._min_x < coordinate.x < self._max_x and self._min_y < coordinate.y < self._max_y


def targets_from_file(path='inputs\\6.txt') -> Iterable[Coordinate]:
    """Return a list of targets which are stored in a file, each target in its own line.
    :param path: path of file with targets
    :return: list of targets from file
    """
    with open(path) as file:
        for line in file:
            x, y = line.replace(' ', '').split(',')
            yield Coordinate(int(x), int(y))


def min_max(integers: Iterable[int]) -> Tuple[int, int]:
    integers, integers_ = tee(integers)
    return min(integers), max(integers_)


def enclosing_rectangle(targets: List[Coordinate]) -> Rectangle:
    """
    :return: enclosing rectangle of the grid by given borders.
    """
    xs = (target.x for target in targets)
    ys = (target.y for target in targets)
    min_x, max_x = min_max(xs)
    min_y, max_y = min_max(ys)
    return Rectangle(min_x, max_x, min_y, max_y)


def find_largest_area(targets: List[Coordinate]) -> int:
    """Find for each coordinate its closest target.
    :param targets: target coordinates
    """
    rectangle = enclosing_rectangle(targets)
    # Filter out target coordinates which are on the "enclosing_rectangle" of the grid
    coordinates = [coordinate for coordinate in rectangle.all_coordinates() if coordinate not in targets]

    targets_to_area = {target: [target] for target in targets}

    for coordinate in coordinates:
        closest = closest_target(coordinate, targets)
        if closest is not None:
            targets_to_area[closest].append(coordinate)

    filtered_targets = [target for target in targets_to_area
                        if all(coordinate in rectangle for coordinate in targets_to_area[target])]
    return max([len(targets_to_area[target]) for target in filtered_targets])


def closest_target(coordinate, targets):
    closest = closest_coordinate(coordinate, targets)
    rest = targets[:]
    rest.remove(closest)
    second_closest = closest_coordinate(coordinate, rest)
    if dist(coordinate, closest) != dist(coordinate, second_closest):
        return closest
    else:
        return None


def closest_coordinate(coordinate, coordinates):
    return min(coordinates,
               key=lambda c: dist(coordinate, c))


def dist(c1: Coordinate, c2: Coordinate, abs=abs) -> int:
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])


def main():
    targets = list(targets_from_file())
    largest_area = find_largest_area(targets)
    print(f'Largest area: {largest_area}')


if __name__ == '__main__':
    main()
