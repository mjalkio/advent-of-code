from collections import defaultdict

from util import read_puzzle_input


def _get_bag_rules(puzzle_input):
    lines = [
        # Remove the period
        line[:-1]
        for line
        in puzzle_input.split('\n')
        if line != ''
    ]
    rules = {}
    for line in lines:
        bag_type, contained_bag_details = line.split(' bags contain ')
        if contained_bag_details == 'no other bags':
            rules[bag_type] = {}
            continue

        rules[bag_type] = {
            contained_bag_type.replace(' bags', '').replace(' bag', ''): int(num_bags)
            for num_bags, contained_bag_type
            in [
                contained_bag.split(' ', maxsplit=1)
                for contained_bag
                in contained_bag_details.split(', ')
            ]
        }
    return rules


def _get_bags_that_can_hold(rules):
    bags_that_can_hold = defaultdict(set)
    for bag, contained_bags in rules.items():
        for contained_bag in contained_bags:
            bags_that_can_hold[contained_bag].add(bag)
    return bags_that_can_hold


def num_bags_colors_can_contain_my_bag(puzzle_input, my_bag='shiny gold'):
    rules = _get_bag_rules(puzzle_input)
    bags_that_can_hold = _get_bags_that_can_hold(rules)

    bags_can_contain_my_bag = bags_that_can_hold[my_bag]
    num_bags = len(bags_can_contain_my_bag)
    while True:
        for bag in list(bags_can_contain_my_bag):
            bags_can_contain_my_bag |= bags_that_can_hold[bag]
        if len(bags_can_contain_my_bag) == num_bags:
            break
        num_bags = len(bags_can_contain_my_bag)

    return num_bags


def num_bags_contained_in_my_bag(puzzle_input, my_bag='shiny gold'):
    rules = _get_bag_rules(puzzle_input)
    num_bags_in = {}
    while my_bag not in num_bags_in:
        for bag, contained_bags in rules.items():
            if all([
                contained_bag in num_bags_in
                for contained_bag
                in contained_bags
            ]):
                num_bags_in[bag] = sum(
                    contained_bag_quantity + contained_bag_quantity * num_bags_in[contained_bag]
                    for contained_bag, contained_bag_quantity
                    in contained_bags.items()
                )
    return num_bags_in[my_bag]


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {num_bags_colors_can_contain_my_bag(puzzle_input)}")
    print(f"Part 2: {num_bags_contained_in_my_bag(puzzle_input)}")
