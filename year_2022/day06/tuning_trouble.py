from util import read_puzzle_input


def get_marker_idx(puzzle_input, marker_len):
    idx = marker_len
    while len(set(puzzle_input[idx - marker_len : idx])) != marker_len:
        idx += 1
    return idx


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_marker_idx(puzzle_input, marker_len=4)}")
    print(f"Part 2: {get_marker_idx(puzzle_input, marker_len=14)}")
