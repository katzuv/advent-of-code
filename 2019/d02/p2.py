import itertools

import p1


def main():
    original_numbers = p1.get_numbers_from_input()
    for noun, verb in itertools.product(range(100), range(100)):
        numbers = original_numbers
        numbers[1] = noun
        numbers[2] = verb
        output = p1.program_output(numbers)
        if output == 19690720:
            print(f'100 * noun + verb = {100 * noun + verb}')


if __name__ == '__main__':
    main()
