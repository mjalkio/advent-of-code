from util import read_puzzle_input


def is_ordered(left, right):
    return False


def sum_indices_ordered_pairs(puzzle_input):
    pairs = puzzle_input.split("\n\n")

    result = 0
    for i, pair in enumerate(pairs):
        left, right = pair.split("\n")
        if is_ordered(left, right):
            result += i + 1
    return result


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {sum_indices_ordered_pairs(puzzle_input)}")
    print(f"Part 2: {sum_indices_ordered_pairs(puzzle_input)}")
