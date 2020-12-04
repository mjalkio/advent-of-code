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
):
    for field in required_fields:
        if f"{field}:" not in passport:
            return False
    return True


def num_valid_passports(passport_batch):
    passports = passport_batch_to_tuple(passport_batch)
    return sum(passport_is_valid(passport) for passport in passports)


if __name__ == '__main__':
    puzzle_input_path = Path(Path(__file__).parent, 'puzzle_input.txt')
    with puzzle_input_path.open() as f:
        puzzle_input = f.read()

    print(f"Part 1: {num_valid_passports(passport_batch=puzzle_input)}")
