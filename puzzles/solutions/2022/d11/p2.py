import sys
from pathlib import Path
from typing import Iterable

from monkey import Monkey


SOLUTIONS_DIRECTORY = str(Path(__file__).resolve().parents[2])
sys.path.insert(0, SOLUTIONS_DIRECTORY)
from utils import crt


def modify_worry_level(worry_level: int, monkeys: Iterable[Monkey]) -> int:
    moduli_to_remainders = {
        current_monkey.test_divisor: worry_level % current_monkey.test_divisor
        for current_monkey in monkeys
    }
    return crt.calculate_chinese_remainder_theorem(moduli_to_remainders)


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.
