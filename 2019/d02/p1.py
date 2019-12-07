from typing import List


def get_program_from_input():
    with open('../inputs/2.txt') as input_file:
        numbers = [int(number) for number in input_file.read().split(',')]
    return numbers


class IntcodeComputer:
    OPCODES_TO_AMOUNT_OF_PARAMS = {1: 3, 2: 3, 3: 2, 4: 1}

    def __init__(self, program: List[int]):
        self.program = program

    def add_opcode(self, opcode: int, amount_of_params: int):
        self.OPCODES_TO_AMOUNT_OF_PARAMS[opcode] = amount_of_params

    def program_output(self) -> int:
        self._run_program()
        return self.program[0]

    def _run_program(self):
        indexes = iter(range(0, len(self.program)))
        for i in indexes:
            opcode = self.program[i]
            if opcode == 99:
                return
            try:
                amount = self.OPCODES_TO_AMOUNT_OF_PARAMS[opcode]
            except KeyError:
                raise NotImplementedError(f'opcode {opcode} is not yet supported')
            self._run_instruction(opcode, self.program[i + 1: i + 1 + amount])
            for _ in range(amount):
                next(indexes)

    def _run_instruction(self, opcode: int, parameters: List[int]):
        getattr(self, f'_run_opcode_{opcode}')(parameters)

    def _run_opcode_1(self, parameters: List[int]):
        first = self.program[parameters[0]]
        second = self.program[parameters[1]]
        self.program[parameters[2]] = first + second

    def _run_opcode_2(self, parameters: List[int]):
        first = self.program[parameters[0]]
        second = self.program[parameters[1]]
        self.program[parameters[2]] = first * second


def main():
    program = get_program_from_input()
    program[1] = 12
    program[2] = 2
    computer = IntcodeComputer(program)
    print(f'Value at position 0: {computer.program_output()}')


if __name__ == '__main__':
    main()
