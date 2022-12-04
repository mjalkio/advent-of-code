from util import read_puzzle_input
from year_2022.day04.camp_cleanup import (
    num_fully_contained_assignments,
)


def test_num_fully_contained_assignments():
    assert num_fully_contained_assignments(read_puzzle_input("test_input.txt")) == 2
