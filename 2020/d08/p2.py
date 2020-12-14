from p1 import get_program_from_input, INPUT_FILE_PATH
from src import GameConsole


def change_instruction(program: list[str], index: int):
    current_instruction = program[index]
    operation, argument = current_instruction.split()

    operation = 'nop' if operation == 'jmp' else 'jmp'
    argument = int(argument)

    program[index] = f'{operation} {argument}'


def main():
    input_text = INPUT_FILE_PATH.read_text()
    program = get_program_from_input(input_text)

    changeable_instructions_indices = [i for i in range(len(program)) if 'acc' not in program[i]]
    last_instruction_changed_index = changeable_instructions_indices[0]
    change_instruction(program, last_instruction_changed_index)
    for index in changeable_instructions_indices:
        change_instruction(program, last_instruction_changed_index)
        change_instruction(program, index)
        last_instruction_changed_index = index

        game_console = GameConsole(program)
        if game_console.run():
            break

    print(f'Accumulator value after the program terminates: {game_console.get_accumulator_value()}')


if __name__ == '__main__':
    main()
