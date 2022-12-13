import sys
from typing import Sequence

from stack import Stack
from step import Step


def execute_transfer_step(stacks: Sequence[Stack], step: Step):
    """
    Process a transferring of crates between stacks.
    :param stacks: sequence of `Stack`s
    :param step: step to execute
    """
    crates = stacks[step.src - 1].remove_crates(step.amount)
    stacks[step.dst - 1].add_crates(
        reversed(tuple(crates))
    )  # Reverse the crates because now they now retain their order when transferred.


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
