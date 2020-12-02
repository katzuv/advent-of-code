import re
from typing import Sequence

from p1 import get_passwords_from_input


class Password:
    _REQUIRED_POSITION_TO_CONTAIN_LETTER = 1

    def __init__(self, password: str):
        properties = self._get_password_properties(password)
        self._first_index = int(properties[0])
        self._second_index = int(properties[1])
        self._letter = properties[2]
        self._password_text = properties[3]

    @staticmethod
    def _get_password_properties(password: str) -> Sequence[str]:
        return re.match(r'(\d+)-(\d+) (\w): (\w+)', password).groups()

    def is_password_valid(self) -> bool:
        first_letter = self._get_letter_in_position(self._first_index)
        second_letter = self._get_letter_in_position(self._second_index)

        letters = first_letter + second_letter
        letter_amount_in_positions = letters.count(self._letter)
        return letter_amount_in_positions == self._REQUIRED_POSITION_TO_CONTAIN_LETTER

    def _get_letter_in_position(self, position: int) -> str:
        return self._password_text[position - 1]  # Toboggan Corporate Policies have no concept of "index zero"


def main():
    passwords_input = get_passwords_from_input()
    passwords = list(map(Password, passwords_input))

    valid_passwords = sum(password.is_password_valid() for password in passwords)
    print(f'Amount of valid passwords: {valid_passwords}')


if __name__ == '__main__':
    main()
