import sys

from p1 import Graph


def sort_update(update: list[str], order: Graph) -> list[str]:
    page_numbers = set(update)
    needed_order = {
        page_number: order[page_number] & page_numbers for page_number in update
    }
    sorted_update = []
    while len(sorted_update) < len(update):
        for page_number in update:
            if page_number in sorted_update:
                continue
            dependencies = needed_order[page_number]
            if dependencies <= set(sorted_update):
                sorted_update.append(page_number)
    return sorted_update


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
