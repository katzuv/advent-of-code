from pathlib import Path

INPUT_FILE_PATH = Path('..', 'inputs', '6.txt')
GROUPS_SEPARATOR = '\n\n'


def get_groups_from_input(input_text: str) -> list:
    return input_text.split(GROUPS_SEPARATOR)


def get_positive_answers_from_groups(group: str) -> set:
    group = group.replace('\n', '')
    return set(group)


def main():
    input_text = INPUT_FILE_PATH.read_text()

    groups = get_groups_from_input(input_text)

    groups_answers = map(get_positive_answers_from_groups, groups)
    total_positive_answers = sum(len(group) for group in groups_answers)
    print(f'Sum of questions answered "yes" to: {total_positive_answers}')


if __name__ == '__main__':
    main()
