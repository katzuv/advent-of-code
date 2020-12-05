from p1 import get_seats_ids, get_seats_from_input, INPUT_FILE_PATH


def main():
    seats_input = INPUT_FILE_PATH.read_text()
    seats = get_seats_from_input(seats_input)

    seats_ids = get_seats_ids(seats)

    seats_ids.sort()
    for i, seat_id in enumerate(seats_ids):
        if seats_ids[i + 1] - seat_id == 2:  # My seat is missing from the list, so if there is a seat id
            missing_seat_id = seat_id + 1
            break

    print(f'My seat id: {missing_seat_id}')


if __name__ == '__main__':
    main()
