from util import read_puzzle_input


def is_valid(password):
    return 0


def get_num_valid_passwords(puzzle_input):
    min_password, max_password = [int(password) for password in puzzle_input.split("-")]
    return len(
        password
        for password in range(min_password, max_password + 1)
        if is_valid(str(password))
    )


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_num_valid_passwords(puzzle_input)}")
    print(f"Part 2: {get_num_valid_passwords(puzzle_input)}")
