from collections import Counter

from util import read_puzzle_input


def _apply_rules(rules, polymer):
    if polymer in rules:
        return rules[polymer]

    if len(polymer) <= 1:
        return polymer

    split_idx = len(polymer) // 2
    left_side = _apply_rules(rules, polymer[:split_idx])
    right_side = _apply_rules(rules, polymer[split_idx + 1 :])

    if left_side[-1] + polymer[split_idx] in rules:
        left_side = left_side + rules[left_side[-1] + polymer[split_idx]]

    if polymer[split_idx] + right_side[0] in rules:
        right_side = rules[polymer[split_idx] + right_side[0]] + right_side

    new_polymer = left_side + polymer[split_idx] + right_side
    rules[polymer] = new_polymer
    return new_polymer


def get_difference_most_least_common_element_counts(puzzle_input, num_steps=10):
    polymer, rules = puzzle_input.split("\n\n")
    rules = dict([rule.split(" -> ") for rule in rules.split("\n")])

    for _ in range(num_steps):
        polymer = _apply_rules(rules, polymer)

    element_counts = Counter(polymer)
    return max(element_counts.values()) - min(element_counts.values())


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_difference_most_least_common_element_counts(puzzle_input)}")
    print(
        f"Part 2: {get_difference_most_least_common_element_counts(puzzle_input, num_steps=40)}"
    )
