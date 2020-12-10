from p1 import get_positive_answers_from_groups, get_groups_from_input, INPUT_FILE_PATH
from collections import Counter

INNER_GROUP_SEPARATOR = '\n'


def get_group_size(group: str) -> int:
    return group.count(INNER_GROUP_SEPARATOR) + 1


def get_group_answers_by_amount(group: str) -> Counter:
    only_letters = ''.join(filter(str.isalpha, group))
    counter = Counter(only_letters.lower())
    return counter


def get_questions_amount_all_answered_yes(group: str) -> int:
    answer_to_amount = get_group_answers_by_amount(group)
    group_size = get_group_size(group)
    questions_everyone_answered_yes = 0
    for answer_amount in answer_to_amount.values():
        if answer_amount == group_size:
            questions_everyone_answered_yes += 1

    return questions_everyone_answered_yes


def main():
    input_text = INPUT_FILE_PATH.read_text().strip()  # The input ends with a '\n', so strip it to make sure the group
    # size works correctlly for all groups.

    groups = get_groups_from_input(input_text)

    total = sum(map(get_questions_amount_all_answered_yes, groups))
    print(f'Total amount of questions everyone in their group answered positively: {total}')


if __name__ == '__main__':
    main()
