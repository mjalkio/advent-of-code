from util import read_puzzle_input
from year_2022.day04.camp_cleanup import (
    num_fully_contained_assignments,
    num_overlapping_pairs,
)


def test_num_fully_contained_assignments():
    assert num_fully_contained_assignments(read_puzzle_input("test_input.txt")) == 2


def test_num_overlapping_pairs():
    assert num_overlapping_pairs(read_puzzle_input("test_input.txt")) == 4
