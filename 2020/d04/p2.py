import re

from p1 import get_passports_from_input, FIELDS_WITHOUT_PID, INPUT_FILE_PATH


class Passport:
    _KEY_VALUE_SEPARATOR = ':'

    class _Requirements:
        YEAR_LENGTH = 4
        BIRTH_YEAR = (1920, 2002)
        ISSUE_YEAR = (2010, 2020)
        EXPIRATION_YEAR = (2020, 2030)

        CM = 'cm'
        IN = 'in'
        HEIGHTS = {CM: (150, 193), IN: (59, 76)}

        EYE_COLORS = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')

        PASSPORT_ID_LENGTH = 9

    def __init__(self, passport_text: str):
        if not self._are_required_fields_present(passport_text):
            raise ValueError('Passport does not contain all required fields')

        keys_values = self._get_fields_with_values(passport_text)
        for key, value in keys_values.items():
            setattr(self, f'_{key}', value)

    @staticmethod
    def _are_required_fields_present(passport_text: str) -> bool:
        return all(field in passport_text for field in FIELDS_WITHOUT_PID)

    @classmethod
    def _get_fields_with_values(cls, passport_text: str) -> dict[str: str]:
        items = passport_text.split()
        keys_values = {}
        for item in items:
            key, value = item.split(cls._KEY_VALUE_SEPARATOR)
            keys_values[key] = value
        return keys_values

    def is_valid(self) -> bool:
        return all(getattr(self, f'_is_{field}_valid')() for field in FIELDS_WITHOUT_PID)

    @classmethod
    def _is_year_length_valid(cls, year: str):
        return len(year) == cls._Requirements.YEAR_LENGTH

    def _is_byr_valid(self):
        if not self._is_year_length_valid(self._byr):
            return False
        return self._Requirements.BIRTH_YEAR[0] <= int(self._byr) <= self._Requirements.BIRTH_YEAR[1]

    def _is_iyr_valid(self):
        if not self._is_year_length_valid(self._iyr):
            return False
        return self._Requirements.ISSUE_YEAR[0] <= int(self._iyr) <= self._Requirements.ISSUE_YEAR[1]

    def _is_eyr_valid(self):
        if not self._is_year_length_valid(self._eyr):
            return False
        return self._Requirements.EXPIRATION_YEAR[0] <= int(self._eyr) <= self._Requirements.EXPIRATION_YEAR[1]

    def _is_hgt_valid(self):
        try:
            height, unit = re.match(r'^(\d+)(cm|in)$', self._hgt).groups()
        except AttributeError:  # Field value doesn't match pattern.
            return False

        for valid_unit in self._Requirements.HEIGHTS:
            if unit == valid_unit:
                valid_heights = self._Requirements.HEIGHTS[valid_unit]
                return valid_heights[0] <= int(height) <= valid_heights[1]

        return False

    def _is_hcl_valid(self):
        return re.match(r'^#[0-9a-f]{6}', self._hcl)

    def _is_ecl_valid(self):
        return self._ecl in self._Requirements.EYE_COLORS

    def _is_pid_valid(self):
        return len(self._pid) == self._Requirements.PASSPORT_ID_LENGTH


def main():
    input_text = INPUT_FILE_PATH.read_text()
    passports = get_passports_from_input(input_text)

    valid_passports = 0
    for passport in passports:
        try:
            valid_passports += Passport(passport).is_valid()
        except ValueError:
            pass
    print(f'Valid passports: {valid_passports}')


if __name__ == '__main__':
    main()
