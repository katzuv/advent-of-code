import re
import sys


def calculate_calibration_values_sum(input_text: str) -> int:
    calibration_values_sum = 0
    for line in input_text.splitlines():
        numbers = re.findall(r"\d", line)
        calibration_value = int(numbers[0]) * 10 + int(numbers[-1])
        calibration_values_sum += calibration_value
    return calibration_values_sum


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
