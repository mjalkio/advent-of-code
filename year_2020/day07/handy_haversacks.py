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
            contained_bag_type: int(num_bags)
            for num_bags, contained_bag_type
            in [
                contained_bag.split(' ', maxsplit=1)
                for contained_bag
                in contained_bag_details.split(', ')
            ]
        }
    return rules


def num_bags_colors_can_contain_my_bag(puzzle_input, my_bag='shiny gold'):
    rules = _get_bag_rules(puzzle_input)
    return None


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {num_bags_colors_can_contain_my_bag(puzzle_input)}")
    print(f"Part 2: {None}")
