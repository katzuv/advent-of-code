import dataclasses


@dataclasses.dataclass
class File:
    """A file with a name and size."""

    name: str
