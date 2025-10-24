import sys
def is_modified_report_safe(report: tuple[int, ...]) -> bool:
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1 :]
        if is_report_safe(modified_report):
            return True
    return False


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
