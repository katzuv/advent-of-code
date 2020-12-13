from .instruction_base import InstructionBase


class JumpOperation(InstructionBase):
    def run(self) -> bool:
        self._program_state.vary_instruction_pointer(self._argument)
        return False
