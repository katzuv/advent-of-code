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
