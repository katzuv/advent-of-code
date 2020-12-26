import copy
import itertools

from p1 import count_occupied_seats, count_adjacent_seats_by_types, FLOOR, EMPTY, OCCUPIED, get_grid_from_input, \
    INPUT_FILE_PATH

MINIMAL_EMPTY_ADJACENT_SEATS_AMOUNT_TO_LEAVE = 5

DISPLACEMENTS = list(itertools.product(range(-1, 2), range(-1, 2)))
DISPLACEMENTS.remove((0, 0))


def get_seen_seat(diff: tuple[int, int], row: int, column: int, grid: list[list[str]]) -> str:
    while True:
        row += diff[0]
        column += diff[1]
        if row < 0 or column < 0:
            return FLOOR
        try:
            point = grid[row][column]
        except IndexError:  # Reached end of direction with no seen seats.
            return FLOOR
        if point != FLOOR:
            return point


def get_seen_seats(grid: list[list[str]], row: int, column: int) -> list[str]:
    seen_points = [get_seen_seat(diff, row, column, grid) for diff in DISPLACEMENTS]
    return [point for point in seen_points if point != FLOOR]


def get_seat_next_state(seat: str, other_seats: list[str]) -> str:
    other_seats_by_types_counter = count_adjacent_seats_by_types(other_seats)
    if seat == EMPTY and other_seats_by_types_counter[EMPTY] == len(other_seats):
        return OCCUPIED
    if seat == OCCUPIED and other_seats_by_types_counter[OCCUPIED] >= MINIMAL_EMPTY_ADJACENT_SEATS_AMOUNT_TO_LEAVE:
        return EMPTY
    return seat


def get_new_grid(grid: list[list[str]]) -> list[list[str]]:
    new_grid = copy.deepcopy(grid)
    for row, column in itertools.product(range(len(grid)), range(len(grid[0]))):
        seat = grid[row][column]
        if seat == FLOOR:
            continue
        new_grid[row][column] = get_seat_next_state(seat, get_seen_seats(grid, row, column))
    return new_grid


def get_final_grid(grid):
    while True:
        new_grid = get_new_grid(grid)
        if grid == new_grid:
            break
        grid = new_grid
    return grid


def main():
    input_text = INPUT_FILE_PATH.read_text()
    grid = get_grid_from_input(input_text)

    grid = get_final_grid(grid)

    occupied_seats = count_occupied_seats(grid)
    print(f'Occupied seats: {occupied_seats}')


if __name__ == '__main__':
    main()
