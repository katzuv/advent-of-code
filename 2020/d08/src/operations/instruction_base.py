from abc import ABC, abstractmethod


class InstructionBase(ABC):
    def __init__(self, program_state, argument: int):
        self._program_state = program_state
        self._argument = argument

    @abstractmethod
    def run(self) -> bool:
        """
        Run the instruction with the given parameter.
        :return: whether the program should halt
        """
        pass
