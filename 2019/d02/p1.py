from typing import List


def get_program_from_input(day_number):
    with open(f'../inputs/{day_number}.txt') as input_file:
        numbers = [int(number) for number in input_file.read().split(',')]
    return numbers


class IntcodeComputer:
    OPCODES_TO_AMOUNT_OF_PARAMS = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3}

    def __init__(self, program: List[int]):
        self.program = program
        self._pointer = 0
        self._has_pointer_jumped = False

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

    def _run_instruction(self, opcode: int, parameters: List[int], modes: List[int]):
        getattr(self, f'_run_opcode_{opcode}')(parameters, modes)

    def _run_opcode_1(self, parameters: List[int], modes: List[int]):
        first = self.arg(parameters[0], modes[0])
        second = self.arg(parameters[1], modes[1])
        self.program[parameters[2]] = first + second

    def _run_opcode_2(self, parameters: List[int], modes: List[int]):
        first = self.arg(parameters[0], modes[0])
        second = self.arg(parameters[1], modes[1])
        self.program[parameters[2]] = first * second

    def arg(self, param: int, mode: int):
        if mode == 0:
            return self.program[param]
        elif mode == 1:
            return param
        raise LookupError(f'Parameter mode {mode} is not supported')


def main():
    program = get_program_from_input(2)
    program[1] = 12
    program[2] = 2
    computer = IntcodeComputer(program)
    print(f'Value at position 0: {computer.program_output()}')


if __name__ == '__main__':
    main()
