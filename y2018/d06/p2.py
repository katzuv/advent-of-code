from p1 import targets_from_file, enclosing_rectangle, dist

MAX_TOTAL_DISTANCE = 10000


def total_distance(coordinate, targets):
    return sum(dist(coordinate, target) for target in targets)


def find_largest_area(targets):
    rectangle = enclosing_rectangle(targets)
    return sum(total_distance(coordinate, targets) < MAX_TOTAL_DISTANCE for coordinate in rectangle.all_coordinates())


def main():
    targets = list(targets_from_file())
    largest_area = find_largest_area(targets)
    print(f'Largest area: {largest_area}')


if __name__ == '__main__':
    main()
