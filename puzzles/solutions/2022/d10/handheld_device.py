from typing import Sequence

from cpu import CPU


class HandheldDevice:
    """The handheld device, which has a CPU and a CRT screen."""

    _SCREEN_WIDTH = 40
    _SCREEN_HEIGHT = 6

    _DARK_PIXEL = "."
    _LIT_PIXEL = "#"

    def __init__(self):
        """Instantiate a handheld device."""
        self._cpu = CPU()
        self._screen = [
            [self._DARK_PIXEL] * self._SCREEN_WIDTH for _ in range(self._SCREEN_HEIGHT)
        ]

    def run(self, opcode: str, parameters: Sequence[int]) -> None:
        """
        Run the given instruction.
        :param opcode: instruction opcode
        :param parameters: instruction parameters
        """
        self._cpu.run(opcode, parameters)

    @property
    def is_ready_for_next(self) -> bool:
        return self._cpu.is_ready_for_next
