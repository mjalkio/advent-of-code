from util import read_puzzle_input
from year_2022.day16.proboscidea_volcanium import (
    most_pressure_possible,
)


def test_most_pressure_possible():
    assert most_pressure_possible(read_puzzle_input("test_input.txt")) == 1651
