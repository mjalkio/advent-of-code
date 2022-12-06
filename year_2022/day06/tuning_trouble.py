from util import read_puzzle_input


def get_first_market_idx(puzzle_input):
    idx = 4
    while len(set(puzzle_input[idx - 4 : idx])) != 4:
        idx += 1
    return idx


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_first_market_idx(puzzle_input)}")
    print(f"Part 2: {get_first_market_idx(puzzle_input)}")
