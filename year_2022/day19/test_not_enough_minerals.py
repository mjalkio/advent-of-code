from util import read_puzzle_input
from year_2022.day19.not_enough_minerals import (
    sum_quality_levels,
)


def test_sum_quality_levels():
    assert sum_quality_levels(read_puzzle_input("test_input.txt")) == 33
