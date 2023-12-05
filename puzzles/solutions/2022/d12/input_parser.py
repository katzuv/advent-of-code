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
