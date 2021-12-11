from util import read_puzzle_input


def count_depth_increases(puzzle_input):
    depths = [
        int(measurement)
        for measurement in puzzle_input.split("\n")
        if measurement != ""
    ]

    num_increases = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            num_increases += 1
    return num_increases


def count_sliding_window_depth_increases(puzzle_input):
    depths = [
        int(measurement)
        for measurement in puzzle_input.split("\n")
        if measurement != ""
    ]

    num_increases = 0
    for i in range(1, len(depths) - 1):
        if sum(depths[i : i + 3]) > sum(depths[i - 1 : i + 2]):
            num_increases += 1
    return num_increases


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {count_depth_increases(puzzle_input)}")
    print(f"Part 2: {count_sliding_window_depth_increases(puzzle_input)}")
