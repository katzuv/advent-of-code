import sys

import p1


START_OF_MESSAGE_MINIMUM_UNIQUE_SEQUENCE_LENGTH = 14


def get_answer(input_text: str):
    """Return how many characters need to be processed before the first start-of-message marker is detected."""
    return p1.get_unique_sequence_start_index(input_text, START_OF_MESSAGE_MINIMUM_UNIQUE_SEQUENCE_LENGTH)

if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
