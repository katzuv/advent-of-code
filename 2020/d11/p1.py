import collections
import copy
import itertools
from pathlib import Path

FLOOR = '.'
EMPTY = 'L'
OCCUPIED = '#'

MINIMAL_EMPTY_ADJACENT_SEATS_AMOUNT_TO_LEAVE = 4

INPUT_FILE_PATH = Path('..', 'inputs', '11.txt')


def get_grid_from_input(input_text: str) -> list[list[str]]:
    return [list(line) for line in input_text.splitlines()]


def get_adjacent_seats(grid: list[list[str]], row: int, column: int) -> list[str]:
    min_row = max(0, row - 1)
    max_row = min(len(grid) - 1, row + 1)
    min_column = max(0, column - 1)
    max_column = min(len(grid[0]) - 1, column + 1)

    adjacent_seats = [grid[current_row][current_column] for current_row, current_column in
                      itertools.product(range(min_row, max_row + 1), range(min_column, max_column + 1))]
    adjacent_seats.remove(grid[row][column])  # Remove the seat which was passed to the function.
    adjacent_seats = [seat for seat in adjacent_seats if seat != FLOOR]
    return adjacent_seats


def count_adjacent_seats_by_types(adjacent_seats: list[str]) -> collections.Counter:
    return collections.Counter(adjacent_seats)


def get_seat_next_state(seat: str, other_seats: list[str]) -> str:
    other_seats_by_types_counter = count_adjacent_seats_by_types(other_seats)
    if seat == EMPTY and other_seats_by_types_counter[EMPTY] == len(other_seats):
        return OCCUPIED
    if seat == OCCUPIED and other_seats_by_types_counter[OCCUPIED] >= MINIMAL_EMPTY_ADJACENT_SEATS_AMOUNT_TO_LEAVE:
        return EMPTY
    return seat


def count_occupied_seats(grid: list[list[str]]) -> int:
    return sum(
        grid[row][column] == OCCUPIED for row, column in itertools.product(range(len(grid)), range(len(grid[0]))))


def get_new_grid(grid: list[list[str]]) -> list[list[str]]:
    new_grid = copy.deepcopy(grid)
    for row, column in itertools.product(range(len(grid)), range(len(grid[0]))):
        seat = grid[row][column]
        if seat == FLOOR:
            continue
        new_grid[row][column] = get_seat_next_state(seat, get_adjacent_seats(grid, row, column))
    return new_grid


def main():
    input_text = INPUT_FILE_PATH.read_text()
    grid = get_grid_from_input(input_text)

    grid = get_final_grid(grid)

    occupied_seats = count_occupied_seats(grid)
    print(f'Occupied seats: {occupied_seats}')


def get_final_grid(grid):
    while True:
        new_grid = get_new_grid(grid)
        if grid == new_grid:
            break
        grid = new_grid
    return grid


if __name__ == '__main__':
    main()
