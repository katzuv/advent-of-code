import sys
from typing import Iterator

from cpu import CPU


def get_instructions(input_text: str) -> Iterator[tuple[str, tuple[int, ...]]]:
    """
    :param input_text: puzzle input
    :return: generator of instructions and their parameters
    """
    for line in input_text.splitlines():
        instruction, *parameters = line.split()
        yield instruction, tuple(map(int, parameters))


def get_answer(input_text: str):
    """Return the sum of signal strengths during the 20th, 60th, 100th, 140th, 180th, and 220th cycles of the CPU."""
    cpu = CPU()
    instructions = get_instructions(input_text)
    instruction = next(instructions)
    while True:
        instruction_opcode, parameters = instruction
        cpu.run(instruction_opcode, parameters)
        if cpu.is_ready_for_next:
            try:
                instruction = next(instructions)
            except StopIteration:
                break

    return cpu.interesting_signal_strengths_sum


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
