from util import read_puzzle_input
from year_2023.day09.mirage_maintenance import (
    sum_extrapolated_values,
)


def test_sum_extrapolated_values():
    assert sum_extrapolated_values(read_puzzle_input("test_input.txt")) == 114


def test_sum_extrapolated_values_backwards():
    assert (
        sum_extrapolated_values(read_puzzle_input("test_input.txt"), backwards=True)
        == 2
    )
