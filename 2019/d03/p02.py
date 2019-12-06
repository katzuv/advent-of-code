import p01


def intersections_by_steps(intersections, path):
    return sorted(intersections, key=path.index)


def main():
    first_path, second_path = p01.get_wires_paths()
    first_path_points = p01.get_points_from_path(first_path)
    second_path_points = p01.get_points_from_path(second_path)
    intersections = p01.get_intersections(first_path_points, second_path_points)

    closest_intersection = min(intersections,
                               key=lambda i: first_path_points.index(i) + second_path_points.index(i))
    min_distance = first_path_points.index(closest_intersection) + second_path_points.index(closest_intersection)
    print(f'Manhattan distance from the central port to the closest intersection by steps number: {min_distance}')


if __name__ == '__main__':
    main()
