import sys

import p1


def get_answer(input_text: str):
    fresh_products, _ = p1.get_products(input_text)
    fresh_products = p1.merge_fresh_product_ranges(fresh_products)

    return sum((r.stop - r.start) for r in fresh_products)


if __name__ == "__main__":
    puzzle_input = sys.argv[1] if len(sys.argv) > 1 else p1.input_example
    print(get_answer(puzzle_input))
