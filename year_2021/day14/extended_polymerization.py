from collections import Counter
from copy import copy

from util import read_puzzle_input


def get_difference_most_least_common_element_counts(puzzle_input, num_steps=10):
    polymer, rule_input = puzzle_input.split("\n\n")
    pair_counts = Counter(polymer[i : i + 2] for i in range(len(polymer) - 1))
    rules = dict([rule.split(" -> ") for rule in rule_input.split("\n")])

    for _ in range(num_steps):
        new_counts = copy(pair_counts)
        for pair, count in pair_counts.items():
            insertion_element = rules[pair]
            new_counts[pair[0] + insertion_element] += count
            new_counts[insertion_element + pair[1]] += count
            new_counts[pair] -= count
        pair_counts = new_counts

    element_counts = Counter()
    for pair, count in pair_counts.items():
        element_counts[pair[0]] += count
        element_counts[pair[1]] += count

    element_counts[polymer[0]] += 1
    element_counts[polymer[-1]] += 1
    for element in element_counts:
        element_counts[element] //= 2
    return max(element_counts.values()) - min(element_counts.values())


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_difference_most_least_common_element_counts(puzzle_input)}")
    print(
        f"Part 2: {get_difference_most_least_common_element_counts(puzzle_input, num_steps=40)}"
    )
