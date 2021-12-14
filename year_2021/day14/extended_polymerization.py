from collections import Counter

from util import read_puzzle_input


def get_difference_most_least_common_element_counts(puzzle_input, num_steps=10):
    polymer, rules = puzzle_input.split("\n\n")
    polymer = polymer
    rules = dict([rule.split(" -> ") for rule in rules.split("\n")])

    for _ in range(num_steps):
        i = len(polymer) - 2
        while i >= 0:
            pair = polymer[i : i + 2]
            if pair in rules:
                polymer = polymer[: i + 1] + rules[pair] + polymer[i + 1 :]
            i -= 1

    element_counts = Counter(polymer)
    return max(element_counts.values()) - min(element_counts.values())


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_difference_most_least_common_element_counts(puzzle_input)}")
    print(
        f"Part 2: {get_difference_most_least_common_element_counts(puzzle_input, num_steps=40)}"
    )
