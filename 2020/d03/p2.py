from p1 import get_grid_from_input, TREE


def count_trees(grid: list[str], distance_moving_right: int, distance_moving_down: int) -> int:
    trees_encountered = 0
    x_location = 0
    row_length = len(grid[0])
    for row in grid[::distance_moving_down]:
        if row[x_location % row_length] == TREE:
            trees_encountered += 1
        x_location += distance_moving_right
    return trees_encountered


def main():
    grid = get_grid_from_input()

    slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    product = 1
    for distance_moving_right, distance_moving_down in slopes:
        product *= count_trees(grid, distance_moving_right, distance_moving_down)
    print(f'Product of trees encountered on each of the listed slopes: {product}')


if __name__ == '__main__':
    main()
