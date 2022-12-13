import re

import consts
from stack import Stack
from step import Step


def get_starting_stacks(stacks_input: str) -> tuple[Stack]:
    """
    :param stacks_input: stacks part of the puzzle input
    :return: tuple of `Stack`s parsed from the input
    """
    lines = stacks_input.splitlines()
    stacks_amount = int(lines[consts.AMOUNT_LINE_NUMBER][consts.AMOUNT_INDEX_IN_LINE])

    stacks = tuple(Stack(()) for _ in range(stacks_amount))
    stacks_lines = reversed(
        lines[: consts.AMOUNT_LINE_NUMBER]  # Start building stacks from the bottom up.
    )

    for line in stacks_lines:
        for index, stack_number in zip(
            range(
                consts.FIRST_CRATE_INDEX,
                consts.FIRST_CRATE_INDEX + consts.STEP_BETWEEN_CRATES * stacks_amount,
                consts.STEP_BETWEEN_CRATES,
            ),
            range(stacks_amount),
        ):
            character = line[index]
            if (
                character.isalpha()
            ):  # Crates are represented by letters. The other character is a space,
                # which means that no crate is in this line on that stack.
                stacks[stack_number].add_crates(character)

    return stacks


def get_procedure_steps(procedure_input: str) -> tuple[Step]:
    """
    :param procedure_input: procedure steps part of the puzzle input
    :return: tuple of `Step`s parsed from the input
    """
    steps = []
    for line in procedure_input.splitlines():
        values = re.match(
            r"move (?P<amount>\d+) from (?P<src>\d+) to (?P<dst>\d+)", line
        ).groupdict()
        values = {field: int(value) for field, value in values.items()}
        steps.append(Step(**values))
    return tuple(steps)
