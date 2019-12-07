from typing import Tuple, List


def get_wires_paths() -> Tuple[List[str], List[str]]:
    with open('../inputs/3.txt') as input_file:
        first_path = input_file.readline().split(',')
        second_path = input_file.readline().split(',')
        for path in (first_path, second_path):
            path[-1] = path[-1].replace('\n', '')
    return first_path, second_path


def get_points_from_path(path: List[str]) -> List[Tuple[int, int]]:
    points = [(0, 0)]
    for move in path:
        direction, amount = move[0], int(move[1:])
        last_x, last_y = points[-1]
        if direction == 'U':
            for i in range(1, amount + 1):
                points.append((last_x, last_y + i))
        elif direction == 'R':
            for i in range(1, amount + 1):
                points.append((last_x + i, last_y))
        elif direction == 'D':
            for i in range(1, amount + 1):
                points.append((last_x, last_y - i))
        elif direction == 'L':
            for i in range(1, amount + 1):
                points.append((last_x - i, last_y))
    return points


def get_intersections(first_path_points, second_path_points):
    intersections = set(first_path_points) & set(second_path_points) - {(0, 0)}
    return intersections


def main():
    first_path, second_path = get_wires_paths()
    first_path_points = get_points_from_path(first_path)
    second_path_points = get_points_from_path(second_path)

    intersections = get_intersections(first_path_points, second_path_points)
    closest_intersection = (min(intersections, key=lambda p: abs(p[0]) + abs(p[1])))
    min_distance = abs(closest_intersection[0]) + abs(closest_intersection[1])
    print(f'Manhattan distance from the central port to the closest intersection: {min_distance}')


if __name__ == '__main__':
    main()
