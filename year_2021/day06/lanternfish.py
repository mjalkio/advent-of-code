from collections import Counter

from util import read_puzzle_input

RATE = 7
NEW_DELAY = 2


def get_num_lanternfish(puzzle_input, num_days=0):
    fish_cohorts = Counter([int(t) for t in puzzle_input.split(",")])
    for i in range(num_days):
        cohort_idx = i % RATE
        num_new = fish_cohorts[cohort_idx]
        fish_cohorts[cohort_idx] += fish_cohorts[RATE]
        for j in range(NEW_DELAY):
            fish_cohorts[RATE + j] = fish_cohorts[RATE + j + 1]
        fish_cohorts[RATE - 1 + NEW_DELAY] = num_new

    return sum(fish_cohorts.values())


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_num_lanternfish(puzzle_input, num_days=80)}")
    print(f"Part 2: {get_num_lanternfish(puzzle_input, num_days=256)}")
