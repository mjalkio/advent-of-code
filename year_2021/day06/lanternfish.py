from collections import Counter

from util import read_puzzle_input


def get_num_lanternfish(puzzle_input, num_days=0):
    timers = [int(t) for t in puzzle_input.split(',')]
    num_fish = Counter(timers)
    for i in range(num_days):
        pass
    return sum(num_fish.values())


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_num_lanternfish(puzzle_input)}")
    print(f"Part 2: {get_num_lanternfish(puzzle_input)}")
