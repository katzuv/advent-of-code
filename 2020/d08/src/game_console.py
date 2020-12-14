from .operations import AccumulatorOperation, JumpOperation, NoOperationOperation
from .program_state import ProgramState


class GameConsole:
    _OPERATIONS_TO_HANDLERS = {'acc': AccumulatorOperation, 'jmp': JumpOperation, 'nop': NoOperationOperation}

    def __init__(self, code: list[str]):
        self._program_state = ProgramState(code)

    def run(self) -> bool:
        """
        Run the program.
        :return: whether the program terminated successfully (reached the last instruction)
        """
        while True:
            operation_type, argument = self._parse(self._program_state.current_instruction)

            operation_handler = self._OPERATIONS_TO_HANDLERS[operation_type]
            operation_runner = operation_handler(self._program_state, argument)

            should_halt = operation_runner.run()
            if self._program_state.has_instruction_executed_twice() or should_halt:
                return False
            if self._program_state.program_finished:
                return True
            self._program_state.add_current_command_index_to_list()

    @staticmethod
    def _parse(command: str) -> tuple[str, int]:
        operation, argument = command.split()
        argument = int(argument)
        return operation, argument

    def get_accumulator_value(self):
        return self._program_state.accumulator
