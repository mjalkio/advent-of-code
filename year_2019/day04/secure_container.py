from util import read_puzzle_input


def _get_num_repeats(password, start_idx):
    i = start_idx
    repeat_char = password[i]
    while i < len(password):
        if password[i] != repeat_char:
            break
        i += 1
    return i - start_idx


def is_valid(password, strict=False):
    # I assume all passwords provided are in the valid range
    has_double = False
    i = 0
    while i < len(password) - 1:
        if int(password[i]) > int(password[i + 1]):
            return False

        if password[i] == password[i + 1]:
            if strict:
                num_repeats = _get_num_repeats(password, i)
                if num_repeats == 2:
                    has_double = True
                i += num_repeats - 1
                continue
            else:
                has_double = True
        i += 1
    return has_double


def get_num_valid_passwords(puzzle_input, strict=False):
    min_password, max_password = [int(password) for password in puzzle_input.split("-")]
    return len(
        [
            password
            for password in range(min_password, max_password + 1)
            if is_valid(str(password), strict=strict)
        ]
    )


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_num_valid_passwords(puzzle_input)}")
    print(f"Part 2: {get_num_valid_passwords(puzzle_input, strict=True)}")
