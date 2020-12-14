from .instruction_base import InstructionBase


class NoOperationOperation(InstructionBase):
    def run(self) -> bool:
        self._program_state.jump()
        return False
