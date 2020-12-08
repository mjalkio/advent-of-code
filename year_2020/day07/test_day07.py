from year_2020.day07.handy_haversacks import (
    num_bags_colors_can_contain_my_bag,
    num_bags_contained_in_my_bag,
)

TEST_INPUT = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

TEST_INPUT_2 = """
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
"""


def test_num_bags_colors_can_contain_my_bag():
    assert num_bags_colors_can_contain_my_bag(puzzle_input=TEST_INPUT) == 4


def test_num_bags_contained_in_my_bag():
    assert num_bags_contained_in_my_bag(puzzle_input=TEST_INPUT) == 32
    assert num_bags_contained_in_my_bag(puzzle_input=TEST_INPUT_2) == 126
