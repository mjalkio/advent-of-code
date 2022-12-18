from util import read_puzzle_input
from year_2022.day14.regolith_reservoir import (
    num_resting_units,
)


def test_num_resting_units():
    assert num_resting_units(read_puzzle_input("test_input.txt")) == 24


def test_num_resting_units_part_2():
    assert (
        num_resting_units(read_puzzle_input("test_input.txt"), fall_to_floor=True) == 93
    )
