import p01


def main():
    lower_bound, upper_bound = p01.get_passwords_range()

    valid_passwords = 0
    for number in range(int(lower_bound), int(upper_bound) + 1):
        string_number = str(number)
        if len(string_number) != p01.NUMBER_LENGTH:
            continue
        if string_number != ''.join(sorted(string_number)):
            continue
        couples = list(zip(string_number[:-1], string_number[1:]))
        adjacent_couples = [couple for couple in couples if couple[0] == couple[1]]
        if not any(couples.count(couple) == 1 for couple in adjacent_couples):
            continue
        valid_passwords += 1

    print(f'Number of valid passwords: {valid_passwords}')


if __name__ == '__main__':
    main()
