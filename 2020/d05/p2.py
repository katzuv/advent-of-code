from p1 import get_seats_ids, get_seats_from_input, INPUT_FILE_PATH


def get_missing_seat_id(seats_ids: list) -> int:
    seats_ids = sorted(seats_ids)
    for i, seat_id in enumerate(seats_ids):
        if seats_ids[i + 1] - seat_id == 2:
            # All seats are filled except mine, so if there is a pair of following seats IDs whose difference is 2,
            # my seat ID is the one between them.
            missing_seat_id = seat_id + 1
            break


def main():
    seats_input = INPUT_FILE_PATH.read_text()
    seats = get_seats_from_input(seats_input)

    seats_ids = get_seats_ids(seats)
    missing_seat_id = get_missing_seat_id(seats_ids)
    print(f'My seat id: {missing_seat_id}')


if __name__ == '__main__':
    main()
