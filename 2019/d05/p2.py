import d05.p1
from d02.p1 import get_program_from_input


class ThermalEnvironmentSupervisionTerminal(d05.p1.ThermalEnvironmentSupervisionTerminal):
    def _run_opcode_5(self, parameters: list[int], modes: list[int]):
        first = self.arg(parameters[0], modes[0])
        if first == 0:
            return
        second = self.arg(parameters[1], modes[1])
        self._pointer = second
        self._has_pointer_jumped = True

    def _run_opcode_6(self, parameters: list[int], modes: list[int]):
        first = self.arg(parameters[0], modes[0])
        if first != 0:
            return
        second = self.arg(parameters[1], modes[1])
        self._pointer = second
        self._has_pointer_jumped = True

    def _run_opcode_7(self, parameters: list[int], modes: list[int]):
        first = self.arg(parameters[0], modes[0])
        second = self.arg(parameters[1], modes[1])
        # first, second, third = map(self.arg, zip(parameters, modes))
        if first < second:
            self.program[parameters[2]] = 1
        else:
            self.program[parameters[2]] = 0

    def _run_opcode_8(self, parameters: list[int], modes: list[int]):
        first = self.arg(parameters[0], modes[0])
        second = self.arg(parameters[1], modes[1])

        # first, second, third = map(self.arg, zip(parameters, modes))
        self.program[parameters[2]] = 1 if first == second else 0


if __name__ == '__main__':
    ThermalEnvironmentSupervisionTerminal(get_program_from_input(5)).program_output()
