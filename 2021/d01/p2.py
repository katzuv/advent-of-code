from typing import Iterator

_DEFAULT_WINDOW_SIZE = 3


def get_measurements_windows(measurements: Iterator[int], window_size: int = _DEFAULT_WINDOW_SIZE) -> list[tuple[int]]:
    """
    Create sliding windows of measurements and return them.
    Stop when there are not enough measurements to produce a window with the given size.
    :param measurements: measurements to create windows from
    :param window_size: size of every window
    :return: measurements windows
    """
    windows = []
    stop_index = (len(measurements) // window_size) * window_size
    for i in range(stop_index):
        windows.append(measurements[i:i + window_size])
    return windows
