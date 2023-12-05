import collections


Coordinate = collections.namedtuple(
    "Coordinate", ("row", "column", "elevation", "is_start", "is_end")
)


def _create_coordinate(heightmap: list[str], row: int, column: int) -> Coordinate:
    elevation = heightmap[row][column]
    is_start = elevation == "S"
    is_end = elevation == "E"
    if is_start:
        elevation = ord("a")
    elif is_end:
        elevation = ord("z") + 1
    else:
        elevation = ord(elevation)
    return Coordinate(row, column, elevation, is_start, is_end)


def _get_neighbors(position: Coordinate, heightmap: list[str]) -> list[Coordinate]:
    """
    :param position: position to return neighbors of
    :param heightmap: heightmap
    :return: list of neighbors, that is position which are N/S/W/E of the position
    and whose elevation is at most one higher
    """
    upper_row = max(0, position.row - 1)
    lower_row = min(len(heightmap) - 1, position.row + 1)
    left_column = max(0, position.column - 1)
    right_column = min(len(heightmap[0]) - 1, position.column + 1)

    neighbors = {
        (upper_row, position.column),
        (position.row, left_column),
        (lower_row, position.column),
        (position.row, right_column),
    }
    neighbors.discard((position.row, position.column))
    neighbors = [
        _create_coordinate(heightmap, row, column) for row, column in neighbors
    ]
    return [
        neighbor
        for neighbor in neighbors
        if neighbor.elevation - position.elevation <= 1
    ]
