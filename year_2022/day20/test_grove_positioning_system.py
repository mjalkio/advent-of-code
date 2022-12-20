from util import read_puzzle_input
from year_2022.day20.grove_positioning_system import (
    grove_coordinates_sum,
)


def test_grove_coordinates_sum():
    assert grove_coordinates_sum(read_puzzle_input("test_input.txt")) == 3
