from util import read_puzzle_input
from year_2023.day01.trebuchet import (
    sum_calibration_values,
)


def test_sum_calibration_values():
    assert sum_calibration_values(read_puzzle_input("test_input.txt")) == 142
