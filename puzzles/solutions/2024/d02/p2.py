import sys

from p1 import get_reports, is_report_safe


def is_modified_report_safe(report: tuple[int, ...]) -> bool:
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1 :]
        if is_report_safe(modified_report):
            return True
    return False


def get_answer(input_text: str) -> int:
    reports = get_reports(input_text)
    safe_reports = 0
    for report in reports:
        if is_report_safe(report) or is_modified_report_safe(report):
            safe_reports += 1
    return safe_reports


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
