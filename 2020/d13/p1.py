from pathlib import Path

SPLITTER = ','

INPUT_FILE_PATH = Path('..', 'inputs', '13.txt')


def get_notes_from_input(input_text: str) -> tuple[int, list[int]]:
    lines = input_text.splitlines()
    earliest_timestamp = int(lines[0])

    bus_ids = []
    for bus_id in lines[1].split(SPLITTER):
        try:
            bus_ids.append(int(bus_id))
        except ValueError:  # Bus is out of service (marked with an "x").
            pass

    return earliest_timestamp, bus_ids


def get_bus_departure_timestamp_difference(bus_id: int, timestamp: int) -> int:
    if timestamp % bus_id == 0:
        return 0
    last_departure_before_timestamp = (timestamp // bus_id) * bus_id
    first_departure_after_timestamp = last_departure_before_timestamp + bus_id
    difference = first_departure_after_timestamp - timestamp
    return difference


def main():
    input_text = INPUT_FILE_PATH.read_text()
    timestamp, bus_ids = get_notes_from_input(input_text)
    bus_departures_differences = {bus_id: get_bus_departure_timestamp_difference(bus_id, timestamp)
                                  for bus_id in bus_ids}

    earliest_bus = min(bus_departures_differences.items(), key=lambda item: item[1])

    product = earliest_bus[0] * earliest_bus[1]
    print(f"ID of the earliest bus multiplied by the number of minutes you'll need to wait for that bus: {product}")


if __name__ == '__main__':
    main()
