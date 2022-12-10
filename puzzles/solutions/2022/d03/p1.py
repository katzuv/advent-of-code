import sys

def get_rucksacks_compartments(
    input_text: str,
) -> list[tuple[set, set]]:
    """
    :param input_text: puzzle input
    :return: list of (first compartment set, second compartment set) couples
    """
    return [
        (
            set(rucksack[: len(rucksack) // 2]),
            set(rucksack[len(rucksack) // 2 :]),
        )
        for rucksack in input_text.splitlines()
    ]


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
