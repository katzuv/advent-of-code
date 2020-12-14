from .instruction_base import InstructionBase


class AccumulatorOperation(InstructionBase):
    def run(self) -> bool:
        self._program_state.accumulate(self._argument)
        self._program_state.jump()
        return False
