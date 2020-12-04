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


def passport_is_valid(
    passport,
    required_fields=('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid',),
    optional_fields=('cid',),
    check_values=False,
):
    passport_data = {
        pair.split(':')[0]: pair.split(':')[1]
        for pair
        in passport.split(' ')
    }
    for field in required_fields:
        if field not in passport_data:
            return False

    if not check_values:
        return True

    numeric_field_ranges = {
        'byr': (1920, 2002),
        'iyr': (2010, 2020),
        'eyr': (2020, 2030),
        'pid': (0, 999999999),
    }
    for field, (min_value, max_value) in numeric_field_ranges.items():
        if not passport_data[field].isnumeric():
            return False

        numeric_value = int(passport_data[field])
        if numeric_value < min_value or numeric_value > max_value:
            return False

    hgt = passport_data['hgt']
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

    hcl_pattern = re.compile(r'^#[0-9a-f]{6}')
    if not hcl_pattern.match(passport_data['hcl']):
        return False

    if passport_data['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
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
