from pathlib import Path

UPPER_HALF_ROW = 'B'
LOWER_HALF_ROW = 'F'
UPPER_HALF_COLUMN = 'R'
LOWER_HALF_COLUMN = 'L'

ROW_LENGTH = 7
COLUMN_LENGTH = 3

BINARY_BASE = 2
ZERO = '0'
ONE = '1'

INPUT_FILE_PATH = Path('..', 'inputs', '5.txt')


def get_seats_from_input(input_text: str) -> list:
    return input_text.splitlines()


def split_row_column(seat: str) -> tuple:
    return seat[:ROW_LENGTH], seat[ROW_LENGTH:]


def _get_number(string: str, lower_half_symbol: str, upper_half_symbol: str) -> int:
    binary_number = string.replace(lower_half_symbol, ZERO).replace(upper_half_symbol, ONE)
    return int(binary_number, base=BINARY_BASE)


def get_row_number(row: str) -> int:
    return _get_number(row, LOWER_HALF_ROW, UPPER_HALF_ROW)


def get_column_number(column: str) -> int:
    return _get_number(column, LOWER_HALF_COLUMN, UPPER_HALF_COLUMN)


def get_seat_id(row: int, column: int) -> int:
    return row * 8 + column


def get_seats_ids(seats: list) -> list:
    seats_ids = []
    for seat in seats:
        row_text, column_text = split_row_column(seat)

        row_number = get_row_number(row_text)
        column_number = get_column_number(column_text)

        seat_id = get_seat_id(row_number, column_number)
        seats_ids.append(seat_id)
    return seats_ids


def main():
    seats_input = INPUT_FILE_PATH.read_text()
    seats = get_seats_from_input(seats_input)

    seats_ids = get_seats_ids(seats)
    print(f'Highest seat ID: {max(seats_ids)}')


if __name__ == '__main__':
    main()
