import collections


Coordinate = collections.namedtuple(
    "Coordinate", ("row", "column", "elevation", "is_start", "is_end")
)
