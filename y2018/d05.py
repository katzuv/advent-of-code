import string


def do_react(first: str, second: str) -> bool:
    """Return whether two units can react."""
    return first.lower() == second.lower() and first != second


def main():
    with open('inputs\\5.txt') as file:
        original = file.readline().strip()

    print(f'1) Final length: {len(react(original))}')

    print(f'Length of shortest reacted polymer by removing one type: \
          {min(len(react(original.replace(letter, "").replace(letter.upper(),""))) for letter in string.ascii_lowercase)}')


def react(polymer: str) -> str:
    """
    :param polymer: a polymer of units
    :return: the polymer after it was fully reacted
    """
    changed = True
    start = 0
    while changed:
        changed = False
        for i, unit in enumerate(polymer[start:-1], start=start):
            next_unit = polymer[i + 1]
            if do_react(unit, next_unit):
                changed = True
                polymer = polymer[:i] + polymer[i + 2:]
                start = max(0, i - 1)
                break
    return polymer


if __name__ == '__main__':
    main()
