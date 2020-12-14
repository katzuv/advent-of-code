from collections import defaultdict
from pathlib import Path

INPUT_FILE_PATH = Path('..', 'inputs', '10.txt')


def get_adapters_from_input(input_text: str) -> list[int]:
    adapters = [int(number) for number in input_text.splitlines()]
    adapters.sort()
    return adapters


def get_next_adapter(adapter_joltage: int, adapters: list[int]) -> int:
    for adapter in adapters:
        difference = adapter - adapter_joltage
        if difference <= 3:
            return adapter


def main():
    input_text = INPUT_FILE_PATH.read_text()
    adapters = get_adapters_from_input(input_text)

    adapters.insert(0, 0)  # Add the charging outlet's joltage.
    differences = defaultdict(int)
    while len(adapters) > 1:
        current_adapter = adapters.pop(0)
        next_adapter = get_next_adapter(current_adapter, adapters)
        difference = next_adapter - current_adapter
        differences[difference] += 1
        adapters.sort()

    differences[3] += 1  # The device's built-in adapter is always 3 higher than the highest adapter.
    product = differences[1] * differences[3]
    print(f'Number of 1-jolt differences multiplied by the number of 3-jolt differences: {product}')


if __name__ == '__main__':
    main()
