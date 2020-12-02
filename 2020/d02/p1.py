import re
from pathlib import Path
from typing import Sequence, Union

INPUT_FILE_PATH = Path('..', 'inputs', '2.txt')


class Password:
    def __init__(self, password: str):
        properties = self._get_password_properties(password)
        self._min = int(properties[0])
        self._max = int(properties[1])
        self._letter = properties[2]
        self._password_text = properties[3]

    @staticmethod
    def _get_password_properties(password: str) -> Sequence[str]:
        return re.match(r'(\d+)-(\d+) (\w): (\w+)', password).groups()

    def is_password_valid(self) -> bool:
        letter_count = self._password_text.count(self._letter)
        return self._min <= letter_count <= self._max


def get_passwords_from_input(path: Union[str, Path] = INPUT_FILE_PATH) -> list[str]:
    if isinstance(path, str):
        path = Path(path)
    return path.read_text().splitlines()


def main():
    passwords_input = get_passwords_from_input()
    passwords = list(map(Password, passwords_input))

    valid_passwords = sum(password.is_password_valid() for password in passwords)
    print(f'Amount of valid passwords: {valid_passwords}')


if __name__ == '__main__':
    main()
