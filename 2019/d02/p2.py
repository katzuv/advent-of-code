import itertools

import p1


def main():
    original_numbers = p1.get_program_from_input()
    computer = p1.IntcodeComputer(original_numbers)
    for noun, verb in itertools.product(range(100), range(100)):
        program = original_numbers[:]
        program[1] = noun
        program[2] = verb
        computer.program = program
        output = computer.program_output()
        if output == 19690720:
            print(f'100 * noun + verb = {100 * noun + verb}')


if __name__ == '__main__':
    main()
