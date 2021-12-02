from typing import Iterable

from p1 import INPUT_FILE_PATH, get_measurements_from_input, get_depth_measurements_increases


_DEFAULT_WINDOW_SIZE = 3


def get_measurements_windows(measurements: Iterable[int], window_size: int = _DEFAULT_WINDOW_SIZE) -> Iterable[
                                                                                                      tuple[int]]:
    """
    Create sliding windows of measurements and return them.
    Stop when there are not enough measurements to produce a window with the given size.
    :param measurements: measurements to create windows from
    :param window_size: size of every window
    :return: measurements windows
    """
    measurements = list(measurements)
    indented_measurements = (measurements[i:] for i in range(window_size))
    return zip(*indented_measurements)


def main():
    input_text = INPUT_FILE_PATH.read_text()
    measurements = get_measurements_from_input(input_text)
    windows = get_measurements_windows(measurements)
    windows_sums = [sum(window) for window in windows]

    sums_increases = get_depth_measurements_increases(windows_sums)
    print(f'Amount of measurements windows sums which are larger than the previous sum: {sums_increases}')


if __name__ == '__main__':
    main()
