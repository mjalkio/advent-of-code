from util import read_puzzle_input
from year_2022.day03.rucksack_reorganization import (
    sum_of_common_priorities,
)


def test_sum_of_common_priorities():
    assert sum_of_common_priorities(read_puzzle_input("test_input.txt")) == 157
