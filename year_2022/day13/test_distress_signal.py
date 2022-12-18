from util import read_puzzle_input
from year_2022.day13.distress_signal import (
    sum_indices_ordered_pairs,
)


def test_sum_indices_ordered_pairs():
    assert sum_indices_ordered_pairs(read_puzzle_input("test_input.txt")) == 13
