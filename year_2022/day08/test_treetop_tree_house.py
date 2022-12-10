from util import read_puzzle_input
from year_2022.day08.treetop_tree_house import (
    highest_scenic_score,
    num_visible_trees,
)


def test_num_visible_trees():
    assert num_visible_trees(read_puzzle_input("test_input.txt")) == 21


def test_highest_scenic_score():
    assert highest_scenic_score(read_puzzle_input("test_input.txt")) == 8
