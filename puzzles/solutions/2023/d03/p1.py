import sys

from schematic_parser import SchematicParser


def get_answer(input_text: str):
    """Return the sum of all part numbers in the engine schematic."""
    schematic_parser = SchematicParser(input_text)
    part_numbers = schematic_parser.find_part_numbers()
    return sum(part_numbers)


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
