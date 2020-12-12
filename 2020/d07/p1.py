from pathlib import Path
import re

INPUT_FILE_PATH = Path('..', 'inputs', '7.txt')

REQUIRED_BAG = 'shiny gold'


def get_rules_strings_from_input(input_text: str) -> list:
    return input_text.splitlines()


def get_rules_dict(rules_strings: str) -> dict:
    rules = {}
    for rule in get_rules_strings_from_input(rules_strings):
        color, bag_rules = get_bag_details(rule)
        rules[color] = bag_rules
    return rules


def get_bag_details(rule: str) -> tuple:
    containing_bag, all_contained_bags = re.match(r'(\w+ \w+) bags contain (.+)\.', rule).groups()
    rules = {}
    for contained_bag in all_contained_bags.split(', '):
        try:
            amount, color = re.match(r'(\d+) (\w+ \w+) bags?', contained_bag).groups()
            rules[color] = int(amount)
        except AttributeError:  # Bag doesn't contain any other bags.
            pass

    return containing_bag, rules


def does_bag_contain_bag(containing_bag: str, contained_bag: str, rules: dict) -> bool:
    contained_bags = rules[containing_bag]
    if contained_bag in contained_bags:
        return True
    for bag in contained_bags:
        if does_bag_contain_bag(bag, contained_bag, rules):
            return True
    return False


def main():
    input_text = INPUT_FILE_PATH.read_text()
    rules = get_rules_dict(input_text)

    total = sum(does_bag_contain_bag(color, REQUIRED_BAG, rules) for color in rules)
    print(f'Total amount of bags containing required bag: {total}')


if __name__ == '__main__':
    main()
