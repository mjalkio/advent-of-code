from util import read_puzzle_input
from year_2022.day16.proboscidea_volcanium import (
    most_pressure_possible,
    most_pressure_possible_with_elephant,
)


def test_most_pressure_possible():
    assert most_pressure_possible(read_puzzle_input("test_input.txt")) == 1651


def test_most_pressure_possible_with_elephant():
    assert (
        most_pressure_possible_with_elephant(read_puzzle_input("test_input.txt"))
        == 1707
    )
