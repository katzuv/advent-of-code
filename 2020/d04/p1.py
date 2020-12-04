from pathlib import Path

PASSPORT_SEPARATION = '\n\n'

INPUT_FILE_PATH = Path('..', 'inputs', '4.txt')

FIELDS_WITHOUT_PID = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
CID = 'cid'
ALL_FIELDS = FIELDS_WITHOUT_PID + (CID,)


def get_passports_from_input(input_text: str) -> list[str]:
    passports = input_text.split(PASSPORT_SEPARATION)
    return [passport.replace('\n', ' ') for passport in passports]


def is_passport_valid(passport: str) -> bool:
    return all(field in passport for field in FIELDS_WITHOUT_PID)


def main():
    input_text = INPUT_FILE_PATH.read_text()
    passports = get_passports_from_input(input_text)

    valid_passports = sum(map(is_passport_valid, passports))
    print(f'Valid passports: {valid_passports}')


if __name__ == '__main__':
    main()
