from util import read_puzzle_input
from year_2022.day10.cathode_ray_tube import (
    sum_interesting_signal_strengths,
)


def test_sum_interesting_signal_strengths():
    assert (
        sum_interesting_signal_strengths(read_puzzle_input("test_input.txt")) == 13140
    )
