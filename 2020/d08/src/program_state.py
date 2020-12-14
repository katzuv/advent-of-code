class ProgramState:
    def __init__(self, program: list[str]):
        self._program = program
        self._accumulator = 0
        self.instruction_pointer = 0
        self.instructions_visited = []

    @property
    def current_instruction(self):
        return self._program[self.instruction_pointer]

    def accumulate(self, amount: int):
        self._accumulator += amount

    def jump(self, amount: int = 1):
        self.instruction_pointer += amount

    def has_instruction_executed_twice(self):
        return self.instruction_pointer in self.instructions_visited

    @property
    def accumulator(self):
        return self._accumulator

    def add_current_command_index_to_list(self):
        self.instructions_visited.append(self.instruction_pointer)

    @property
    def program_finished(self) -> bool:
        return self.instruction_pointer == len(self._program)
