def passport_batch_to_tuple(passport_batch):
    # Two newlines in a row mean there was a blank line
    passports = passport_batch.split('\n\n')
    return tuple(
        passport.replace('\n', ' ').strip()
        for passport
        in passports
        if passport != ''
    )


def passport_is_valid(passport):
    return None


def num_valid_passports(passport_batch):
    return None
