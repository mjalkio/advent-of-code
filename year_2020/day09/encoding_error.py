from util import read_puzzle_input


def has_pair_that_sums(number, preamble):
    for i in range(len(preamble) - 1):
        for j in range(i + 1, len(preamble)):
            if preamble[i] + preamble[j] == number:
                return True
    return False


def first_invalid_number(puzzle_input, preamble_size=25):
    return None


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {first_invalid_number(puzzle_input)}")
    print(f"Part 2: {None}")
