import sys

from p1 import get_products_sum


def get_relevant_sections(input_text: str) -> list[str]:
    sections = input_text.split("do")
    # At the beginning of the program, `mul` instructions are enabled.
    return [sections[0]] + [
        section for section in sections[1:] if section.startswith("()")
    ]


def get_answer(input_text: str) -> int:
    complete_text = "".join(get_relevant_sections(input_text))
    return get_products_sum(complete_text)


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
