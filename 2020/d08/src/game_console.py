import re

from .operations import AccumulatorOperation, JumpOperation, NoOperationOperation
from .program_state import ProgramState


class GameConsole:
    _OPERATIONS_TO_HANDLERS = {'acc': AccumulatorOperation, 'jmp': JumpOperation, 'nop': NoOperationOperation}

    def __init__(self, code: list[str]):
        self._program_state = ProgramState(code)

    def run(self):
        while True:
            operation, argument = self._parse(self._program_state.current_instruction)

            operation_handler = self._OPERATIONS_TO_HANDLERS[operation]
            operation = operation_handler(self._program_state, argument)

            should_halt = operation.run()
            if self._program_state.has_instruction_executed_twice() or should_halt:
                return
            self._program_state.add_current_command_index_to_list()

    @staticmethod
    def _parse(command: str) -> tuple[str, int]:
        operation, argument = re.match(r'(\w+) ([+-]\d+)', command).groups()
        argument = int(argument)
        return operation, argument

    def get_accumulator_value(self):
        return self._program_state.accumulator
