from p1 import get_first_invalid_number, get_numbers_from_input, INPUT_FILE_PATH

MINIMAL_SET_LENGTH = 2


def main():
    input_text = INPUT_FILE_PATH.read_text()
    numbers = get_numbers_from_input(input_text)
    invalid_number = get_first_invalid_number(numbers)

    numbers_amount = len(numbers)
    for length in range(MINIMAL_SET_LENGTH, numbers_amount + 1):
        for index in range(0, numbers_amount - length + 1):
            sequence = numbers[index:index + length]
            if sum(sequence) == invalid_number:
                encryption_weakness = sum((min(sequence), max(sequence)))
                break

    print(f'Encryption weakness in the XMAS-encrypted list: {encryption_weakness}')


if __name__ == '__main__':
    main()
