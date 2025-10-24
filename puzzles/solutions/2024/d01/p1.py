import sys


def get_location_id_lists(input_text: str) -> tuple[list[int], list[int]]:
    first, second = [], []
    for row in input_text.splitlines():
        first_id, second_id = row.split()
        first.append(int(first_id))
        second.append(int(second_id))
    return first, second


def get_answer(input_text: str) -> int:
    first, second = get_location_id_lists(input_text)
    first.sort()
    second.sort()
    return sum(
        abs(first_id - second_id) for (first_id, second_id) in zip(first, second)
    )


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
