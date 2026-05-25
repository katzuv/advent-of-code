import sys


START_OF_PACKET_MINIMUM_UNIQUE_SEQUENCE_LENGTH = 4

def get_unique_sequence_start_index(datastream: str, minimum_unique_sequence_length:int) -> int:
    """
    :param datastream: datastream to process
    :param minimum_unique_sequence_length: minimum length of a unique sequence
    :return: start index of the first unique sequence
    """
    for index in range(minimum_unique_sequence_length - 1, len(datastream)):
        sequence = datastream[index - minimum_unique_sequence_length:index]
        if len(set(sequence)) == minimum_unique_sequence_length:
            return index


def get_answer(input_text: str):
    """Return how many characters need to be processed before the first start-of-packet marker is detected."""
    return get_unique_sequence_start_index(input_text, START_OF_PACKET_MINIMUM_UNIQUE_SEQUENCE_LENGTH)


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
