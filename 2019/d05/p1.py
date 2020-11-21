import os
import sys
from typing import List

sys.path.insert(0, os.path.abspath('..'))

from d02.p1 import IntcodeComputer, get_program_from_input


class ThermalEnvironmentSupervisionTerminal(IntcodeComputer):
    def _run_opcode_3(self, parameters: List[int], modes: List[int]):
        self.program[parameters[0]] = int(input('Enter input for opcode 3: '))

    def _run_opcode_4(self, parameters: List[int], modes: List[int]):
        address = parameters[0]
        print(f'Value at address {address}: {self.program[address]}')

    def _run_program(self):
        i = 0
        while True:
            instruction = str(self.program[i])
            opcode = int(instruction[-2:])
            if opcode == 99:
                return
            modes = self._pad_modes(instruction, opcode)
            self._run_instruction(opcode, self.program[i + 1: i + 1 + self.OPCODES_TO_AMOUNT_OF_PARAMS[opcode]], modes)

            i += self.OPCODES_TO_AMOUNT_OF_PARAMS[opcode] + 1
            print(i, instruction, sep=', ')

    @classmethod
    def _pad_modes(cls, instruction, opcode):
        existing_modes = [int(mode) for mode in instruction[:-2]]
        missing_modes_count = cls.OPCODES_TO_AMOUNT_OF_PARAMS[opcode] - len(existing_modes)
        return list(existing_modes) + ([0] * missing_modes_count)


if __name__ == '__main__':
    ThermalEnvironmentSupervisionTerminal(get_program_from_input(5)).program_output()
