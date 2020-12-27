import math

from p1 import get_manhattan_distance, get_instructions_from_input, INPUT_FILE_PATH

FORWARD = 'F'
RIGHT = 'R'


def north(x: int, y: int, value: int) -> tuple[int, int]:
    return x, y + value


def south(x: int, y: int, value: int) -> tuple[int, int]:
    return x, y - value


def east(x: int, y: int, value: int) -> tuple[int, int]:
    return x + value, y


def west(x: int, y: int, value: int) -> tuple[int, int]:
    return x - value, y


def forward(ship_x: int, ship_y: int, waypoint_x: int, waypoint_y: int, value: int) -> tuple[int, int]:
    ship_x += waypoint_x * value
    ship_y += waypoint_y * value
    return ship_x, ship_y


WAYPOINT_MOVERS = {'N': north, 'S': south, 'W': west, 'E': east}


def rotate(point_x: int, point_y: int, angle: int):
    sine = math.sin(math.radians(angle))
    cosine = math.cos(math.radians(angle))

    new_x = point_x * cosine - point_y * sine
    new_y = point_x * sine + point_y * cosine

    return round(new_x), round(new_y)


def main():
    input_text = INPUT_FILE_PATH.read_text()
    instructions = get_instructions_from_input(input_text)

    ship_x = 0
    ship_y = 0
    waypoint_x = 10
    waypoint_y = 1

    for action, value in instructions:
        if action in WAYPOINT_MOVERS:
            waypoint_x, waypoint_y = WAYPOINT_MOVERS[action](waypoint_x, waypoint_y, value)
        elif action == FORWARD:
            ship_x, ship_y = forward(ship_x, ship_y, waypoint_x, waypoint_y, value)

        else:
            if action == RIGHT:  # The angle of rotation is CCW, so rotating right a certain angle is equivalent to
                # rotating left the negative angle.
                value *= -1
            waypoint_x, waypoint_y = rotate(waypoint_x, waypoint_y, value)

    distance = get_manhattan_distance(ship_x, ship_y)
    print(f'Distance from the start to the end: {distance}')


if __name__ == '__main__':
    main()
