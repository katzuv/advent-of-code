from pathlib import Path
from typing import Union

INPUT_FILE_PATH = Path('..', 'inputs', '3.txt')

TREE = '#'
DISTANCE_MOVING_RIGHT = 3


def get_grid_from_input(path: Union[Path, str] = INPUT_FILE_PATH) -> list[str]:
    if isinstance(path, str):
        path = Path(path)
    return path.read_text().splitlines()


def count_trees(grid: list[str]) -> int:
    trees_encountered = 0
    x_location = 0
    row_length = len(grid[0])
    for row in grid:
        if row[x_location % row_length] == TREE:
            trees_encountered += 1
        x_location += DISTANCE_MOVING_RIGHT
    return trees_encountered


def main():
    grid = get_grid_from_input()
    encountered_tress = count_trees(grid)
    print(f'Amount of trees encountered: {encountered_tress}')


if __name__ == '__main__':
    main()
