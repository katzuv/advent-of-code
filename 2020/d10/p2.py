import functools

from p1 import get_adapters_from_input, INPUT_FILE_PATH


def get_next_vertices(adapter_joltage: int, adapters: tuple[int]) -> tuple[int]:
    return tuple([adapter for adapter in adapters if 0 < adapter - adapter_joltage <= 3])


@functools.cache
def get_paths_amount(vertex: int, end_vertex: int, vertices: tuple[int]) -> int:
    if vertex == end_vertex:
        return 1
    total = 0
    for next_adapter in get_next_vertices(vertex, vertices):
        total += get_paths_amount(next_adapter, end_vertex, vertices)
    return total


def main():
    input_text = INPUT_FILE_PATH.read_text()
    adapters = get_adapters_from_input(input_text)

    adapters.insert(0, 0)
    adapters.sort()
    adapters = tuple(adapters)

    arrangements = get_paths_amount(0, max(adapters), adapters)
    print(f'Total number of arrangements: {arrangements}')


if __name__ == '__main__':
    main()
