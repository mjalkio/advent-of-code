from util import read_puzzle_input
from year_2023.day03.gear_ratios import (
    sum_part_numbers,
)


def test_sum_part_numbers():
    assert sum_part_numbers(read_puzzle_input("test_input.txt")) == 4361
