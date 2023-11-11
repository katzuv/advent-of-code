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

    def _finish_instruction(self) -> None:
        """Set the cycle in instruction counter to zero and mark the CPU as ready for the next instruction."""
        self._cycle_in_instruction = 0
        self.is_ready_for_next = True
