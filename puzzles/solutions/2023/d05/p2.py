import sys


def does_seed_exist(running_value: int, seeds_ranges: list[range]) -> bool:
    return any(running_value in seed_range for seed_range in seeds_ranges)


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
