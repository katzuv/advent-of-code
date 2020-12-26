from pathlib import Path

INPUT_FILE_PATH = Path('..', 'inputs', '12.txt')


def north(x: int, y: int, direction: int, value: int) -> tuple[int, int, int]:
    return x, y + value, direction


def south(x: int, y: int, direction: int, value: int) -> tuple[int, int, int]:
    return x, y - value, direction


def east(x: int, y: int, direction: int, value: int) -> tuple[int, int, int]:
    return x + value, y, direction


def west(x: int, y: int, direction: int, value: int) -> tuple[int, int, int]:
    return x - value, y, direction


def left(x: int, y: int, direction: int, value: int) -> tuple[int, int, int]:
    return x, y, (direction - value) % 360


def right(x: int, y: int, direction: int, value: int) -> tuple[int, int, int]:
    return x, y, (direction + value) % 360


def forward(x: int, y: int, direction: int, value: int) -> tuple[int, int, int]:
    return FORWARD_ACTIONS[direction](x, y, direction, value)


ACTIONS_TO_FUNCTIONS = {'N': north, 'S': south, 'W': west, 'E': east, 'L': left, 'R': right, 'F': forward}
FORWARD_ACTIONS = {0: north, 90: east, 180: south, 270: west}


def get_instructions_from_input(input_text: str) -> list[tuple[str, int]]:
    instructions = []
    for instruction in input_text.splitlines():
        action = instruction[0]
        value = int(instruction[1:])
        instructions.append((action, value))
    return instructions


def get_manhattan_distance(end_x: int, end_y: int, start_x: int = 0, start_y: int = 0) -> int:
    return abs(end_x - start_x) + abs(end_y - start_y)


def main():
    input_text = INPUT_FILE_PATH.read_text()
    instructions = get_instructions_from_input(input_text)

    x = 0
    y = 0
    direction = 90  # The ship starts by facing east.
    for action, value in instructions:
        x, y, direction = ACTIONS_TO_FUNCTIONS[action](x, y, direction, value)

    distance = get_manhattan_distance(x, y)
    print(f'Distance from the start to the end: {distance}')


if __name__ == '__main__':
    main()
