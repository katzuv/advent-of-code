from typing import List


def get_program_from_input():
    with open('../inputs/2.txt') as input_file:
        numbers = [int(number) for number in input_file.read().split(',')]
    return numbers


class IntcodeComputer:
    def __init__(self, program: List[int]):
        self.program = program

    def program_output(self) -> int:
        self._run_program()
        return self.program[0]

    def _run_program(self):
        for i in range(0, len(self.program), 4):
            opcode = self.program[i]
            if opcode == 99:
                break
            first_parameter, second_parameter, third_parameter = self.program[i + 1: i + 4]
            self._run_instruction(opcode, first_parameter, second_parameter, third_parameter)

    def _run_instruction(self, opcode: int, first_parameter: int, second_parameter: int, third_parameter: int):
        getattr(self, f'_run_opcode_{opcode}')(first_parameter, second_parameter, third_parameter)

    def _run_opcode_1(self, first_parameter: int, second_parameter: int, output_index: int):
        first = self.program[first_parameter]
        second = self.program[second_parameter]
        self.program[output_index] = first + second

    def _run_opcode_2(self, first_parameter: int, second_parameter: int, output_index: int):
        first = self.program[first_parameter]
        second = self.program[second_parameter]
        self.program[output_index] = first * second


def main():
    program = get_program_from_input()
    program[1] = 12
    program[2] = 2
    computer = IntcodeComputer(program)
    print(f'Value at position 0: {computer.program_output()}')


if __name__ == '__main__':
    main()
