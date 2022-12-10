import sys

import p1


def get_answer(input_text: str):
    """Return the number of assignment pairs where the ranges overlap."""
    section_pairs = p1.get_sections(input_text)
    return sum(
        not first_section.isdisjoint(second_section)
        for first_section, second_section in section_pairs
    )


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
