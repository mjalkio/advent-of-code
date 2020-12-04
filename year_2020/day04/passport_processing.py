import re
from pathlib import Path


def passport_batch_to_tuple(passport_batch):
    # Two newlines in a row mean there was a blank line
    passports = passport_batch.split('\n\n')
    return tuple(
        passport.replace('\n', ' ').strip()
        for passport
        in passports
        if passport != ''
    )


def _required_fields_are_present(passport_data, required_fields):
    for field in required_fields:
        if field not in passport_data:
            return False
    return True


def _numeric_fields_are_valid(passport_data):
    numeric_field_ranges = {
        'byr': (1920, 2002),
        'iyr': (2010, 2020),
        'eyr': (2020, 2030),
        'pid': (0, 999999999),
    }
    for field, (min_value, max_value) in numeric_field_ranges.items():
        if not passport_data[field].isdigit():
            return False

        numeric_value = int(passport_data[field])
        if numeric_value < min_value or numeric_value > max_value:
            return False

    if len(passport_data['pid']) != 9:
        return False

    return True


def _hgt_is_valid(hgt):
    if 'in' in hgt:
        min_hgt = 59
        max_hgt = 76
        hgt_value, _ = hgt.split('in')
    elif 'cm' in hgt:
        min_hgt = 150
        max_hgt = 193
        hgt_value, _ = hgt.split('cm')
    else:
        return False

    if not hgt_value.isnumeric():
        return False
    if int(hgt_value) < min_hgt or int(hgt_value) > max_hgt:
        return False
    return True


def _hcl_is_valid(hcl):
    hcl_pattern = re.compile(r'^#[0-9a-f]{6}$')
    if not hcl_pattern.match(hcl):
        return False
    return True


def _ecl_is_valid(ecl):
    return ecl in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')


def passport_is_valid(
    passport,
    required_fields=('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid',),
    check_values=False,
):
    passport_data = {
        pair.split(':')[0]: pair.split(':')[1]
        for pair
        in passport.split(' ')
    }

    if not _required_fields_are_present(
        passport_data=passport_data,
        required_fields=required_fields,
    ):
        return False

    if not check_values:
        return True

    if not _numeric_fields_are_valid(passport_data):
        return False

    if not _hgt_is_valid(passport_data['hgt']):
        return False

    if not _hcl_is_valid(passport_data['hcl']):
        return False

    if not _ecl_is_valid(passport_data['ecl']):
        return False

    return True


def num_valid_passports(passport_batch, check_values=False):
    passports = passport_batch_to_tuple(passport_batch)
    return sum(
        passport_is_valid(passport=passport, check_values=check_values)
        for passport
        in passports
    )


if __name__ == '__main__':
    puzzle_input_path = Path(Path(__file__).parent, 'puzzle_input.txt')
    with puzzle_input_path.open() as f:
        puzzle_input = f.read()

    print(f"Part 1: {num_valid_passports(passport_batch=puzzle_input)}")
    # 113 -> too high
    print(f"Part 2: {num_valid_passports(passport_batch=puzzle_input, check_values=True)}")
