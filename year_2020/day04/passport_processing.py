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
    return None
