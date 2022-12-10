import sys


def get_sections(input_text: str) -> tuple[tuple[set[int], set[int]]]:
    """
    :param input_text: puzzle input
    :return: tuple of (first section IDs, second section IDs) pairs
    """
    pairs = input_text.splitlines()
    sections = []
    for pair in pairs:
        pair_sections = []
        for section_range in pair.split(","):
            start, end = map(int, section_range.split("-"))
            section_ids = set(range(start, end + 1))
            pair_sections.append(section_ids)
        sections.append(tuple(pair_sections))
    return tuple(sections)


def get_answer(input_text: str):
    """Return the number of assignment pairs where one range fully contains the other."""
    section_pairs = get_sections(input_text)
    return sum(
        first_section <= second_section or second_section <= first_section
        for first_section, second_section in section_pairs
    )


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
