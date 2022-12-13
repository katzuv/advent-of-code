import sys
from typing import Sequence

import consts
import input_parsing
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
    """
    Return the crates that end up on top of each stack after the rearrangement procedure completes,
    now when crates retain their order.
    """
    starting_stacks, steps = input_text.split(consts.INPUT_PARTS_SPLITTER)
    stacks = input_parsing.get_starting_stacks(starting_stacks)
    steps = input_parsing.get_procedure_steps(steps)
    for step in steps:
        execute_transfer_step(stacks, step)
    return "".join(stack.top for stack in stacks)


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
