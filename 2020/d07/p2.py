from p1 import INPUT_FILE_PATH, get_rules_dict, REQUIRED_BAG


def inner_bags_amount(color: str, rules: dict):
    total = 1
    for inner_color in rules[color]:
        inner_bag_amount = rules[color][inner_color]
        total += inner_bag_amount * inner_bags_amount(inner_color, rules)
    return total


def main():
    input_text = INPUT_FILE_PATH.read_text()
    rules = get_rules_dict(input_text)

    total = inner_bags_amount(REQUIRED_BAG, rules) - 1  # Don't count the outermost bag.
    print(f'Total amount of bags inside a {REQUIRED_BAG} bag: {total}')


if __name__ == '__main__':
    main()
