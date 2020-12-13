from instruction_base import InstructionBase


class AccumulatorOperation(InstructionBase):
    def run(self) -> bool:
        self._program_state.vary_accumulator(self._argument)
        self._program_state.vary_instruction_pointer()
        return False
