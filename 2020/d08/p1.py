from pathlib import Path

from src import GameConsole

INPUT_FILE_PATH = Path('..', 'inputs', '8.txt')


def get_program_from_input(input_text: str) -> list[str]:
    return input_text.splitlines()


def main():
    input_text = INPUT_FILE_PATH.read_text()
    program = get_program_from_input(input_text)
    game_console = GameConsole(program)
    game_console.run()
    print(f'Accumulator value before any instruction is executed a second time: {game_console.get_accumulator_value()}')


if __name__ == '__main__':
    main()
