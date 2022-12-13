import dataclasses


@dataclasses.dataclass
class Step:
    """A step of moving crates between stacks."""

    amount: int
    src: int
