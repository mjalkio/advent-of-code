PUBLIC_KEY_SUBJECT_NUMBER = 7


def _transform_subject_number(value, subject_number):
    return (value * subject_number) % 20201227


def get_loop_size(subject_number, public_key):
    loop_size = 0
    value = 1
    while value != public_key:
        value = _transform_subject_number(value=value, subject_number=subject_number)
        loop_size += 1
    return loop_size


def get_encryption_key(public_key_a, public_key_b, public_key_subject_number=PUBLIC_KEY_SUBJECT_NUMBER):
    loop_size_a = get_loop_size(subject_number=public_key_subject_number, public_key=public_key_a)
    encryption_key = 1
    for _ in range(loop_size_a):
        encryption_key = _transform_subject_number(value=encryption_key, subject_number=public_key_b)
    return encryption_key


if __name__ == '__main__':
    print(f"Part 1: {get_encryption_key(10441485, 1004920)}")
    print(f"Part 2: {None}")
