import sys

import p1


DIGITS_NAMES_TO_NUMBERS = dict(
    zip(
        ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine"),
        (map(str, range(1, 10))),
    )
)


def _convert_digits_names_to_numbers(input_text: str) -> str:
    new_text = ""
    for line in input_text.splitlines():
        new_line = line[0]
        for i in range(1, len(line)):
            current_part_of_line = line[: i + 1]
            new_line += line[i]
            for digit_name in DIGITS_NAMES_TO_NUMBERS:
                if current_part_of_line.endswith(digit_name):
                    new_line += DIGITS_NAMES_TO_NUMBERS[digit_name]
        new_text += new_line + "\n"
    return new_text


def get_answer(input_text: str):
    """Return the calibrations values sum where digits names are replaced with numbers."""
    input_text = _convert_digits_names_to_numbers(input_text)
    return p1.calculate_calibration_values_sum(input_text)


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
