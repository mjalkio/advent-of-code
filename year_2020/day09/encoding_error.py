from util import read_puzzle_input


def _parse_input(puzzle_input):
    return [int(line) for line in puzzle_input.split("\n") if line != ""]


def has_pair_that_sums(number, preamble):
    for i in range(len(preamble) - 1):
        for j in range(i + 1, len(preamble)):
            if preamble[i] + preamble[j] == number:
                return True
    return False


def first_invalid_number(puzzle_input, preamble_size=25):
    encrypted_data = _parse_input(puzzle_input)
    for i in range(preamble_size, len(encrypted_data) - preamble_size):
        test_number = encrypted_data[i + preamble_size]
        preamble = encrypted_data[i : i + preamble_size]
        if not has_pair_that_sums(number=test_number, preamble=preamble):
            return test_number
    return None


def encryption_weakness(puzzle_input, preamble_size=25):
    invalid_number = first_invalid_number(puzzle_input, preamble_size=preamble_size)
    encrypted_data = _parse_input(puzzle_input)
    for i in range(len(encrypted_data) - 1):
        for j in range(i + 1, len(encrypted_data)):
            contiguous_set = encrypted_data[i : j + 1]
            if sum(contiguous_set) == invalid_number:
                return max(contiguous_set) + min(contiguous_set)
            elif sum(contiguous_set) > invalid_number:
                break
    return None


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {first_invalid_number(puzzle_input)}")
    print(f"Part 2: {encryption_weakness(puzzle_input)}")
