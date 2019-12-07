NUMBER_LENGTH = 6


def get_passwords_range():
    with open('../inputs/4.txt') as input_file:
        line = input_file.readline()
        lower_bound, upper_bound = line.split('-')
    return lower_bound, upper_bound


def main():
    lower_bound, upper_bound = get_passwords_range()

    valid_passwords = 0
    for number in range(int(lower_bound), int(upper_bound) + 1):
        string_number = str(number)
        if len(string_number) != NUMBER_LENGTH:
            continue
        if string_number != ''.join(sorted(string_number)):
            continue
        if all(couple[0] != couple[1] for couple in zip(string_number[:-1], string_number[1:])):
            continue
        valid_passwords += 1

    print(f'Number of valid passwords: {valid_passwords}')


if __name__ == '__main__':
    main()
