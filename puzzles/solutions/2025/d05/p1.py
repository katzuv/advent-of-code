import sys

input_example = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
""".strip()


def get_products(input_text: str) -> tuple[list[range], list[int]]:
    fresh_products, available_products = input_text.split("\n\n")
    fresh_products_parsed = []
    for line in fresh_products.splitlines():
        start, end = map(int, line.split("-"))
        fresh_products_parsed.append(range(start, end + 1))
    available_products_parsed = [int(line) for line in available_products.splitlines()]

    fresh_products_parsed.sort(key=lambda r: r.start)
    return fresh_products_parsed, available_products_parsed


def merge_fresh_product_ranges(ranges: list[range]) -> list[range]:
    merged = [ranges[0]]
    for product_range in ranges[1:]:
        last = merged[-1]
        if product_range.start <= last.stop:
            merged[-1] = range(last.start, max(last.stop, product_range.stop))
        else:
            merged.append(product_range)
    return merged


def get_answer(input_text: str):
    fresh_products, available_products = get_products(input_text)
    fresh_products = merge_fresh_product_ranges(fresh_products)
    fresh_available_products = []

    for product in available_products:
        for fresh_range in fresh_products:
            if product in fresh_range:
                fresh_available_products.append(product)
                break
            if fresh_range.start > product:
                break

    return len(fresh_available_products)


if __name__ == "__main__":
    puzzle_input = sys.argv[1] if len(sys.argv) > 1 else input_example
    print(get_answer(puzzle_input))
