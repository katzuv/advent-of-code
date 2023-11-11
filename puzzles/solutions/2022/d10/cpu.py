from typing import Sequence


class CPU:
    """The handheld device's CPU."""

    _INITIAL_INTERESTING_CYCLE = 20
    _INTERESTING_CYCLES_DIFFERENCE = 40

    def __init__(self):
        """Instantiate a CPU."""
        self._x_register = 1

        self._cycle = 0
        self._cycle_in_instruction = 0
        self.is_ready_for_next = False

        self._interesting_cycle = self._INITIAL_INTERESTING_CYCLE
        self.interesting_signal_strengths_sum = 0

    @property
    def cycle(self) -> int:
        """
        :return: the current CPU's cycle
        """
        return self._cycle

    @property
    def x_register(self) -> int:
        """
        :return: the current value of the CPU's x register
        """
        return self._x_register

    def run(self, opcode: str, parameters: Sequence[int]) -> None:
        """
        Run the given instruction.

        This method also calculates the signal strength at interesting cycles.
        :param opcode: instruction opcode
        :param parameters: instruction parameters
        """
        self._cycle += 1
        if self.cycle == self._interesting_cycle:
            signal_strength = self.cycle * self.x_register
            self.interesting_signal_strengths_sum += signal_strength
            self._interesting_cycle += self._INTERESTING_CYCLES_DIFFERENCE

        handler = self._INSTRUCTION_TO_HANDLER[opcode]
        handler(self, parameters)

    def _finish_instruction(self) -> None:
        """Set the cycle in instruction counter to zero and mark the CPU as ready for the next instruction."""
        self._cycle_in_instruction = 0
        self.is_ready_for_next = True

    def _noop(self, parameters: Sequence[int]) -> None:
        """Handle `noop` instruction."""
        self._finish_instruction()

    def _addx(self, parameters: Sequence[int]) -> None:
        """Handle `addx` instruction."""
        if self._cycle_in_instruction == 0:
            self._cycle_in_instruction += 1
            self.is_ready_for_next = False
            return
        self._x_register += parameters[0]
        self._finish_instruction()

    _INSTRUCTION_TO_HANDLER = {"noop": _noop, "addx": _addx}
