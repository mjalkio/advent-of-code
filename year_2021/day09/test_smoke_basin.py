from util import read_puzzle_input
from year_2021.day09.smoke_basin import (
    get_low_point_risk_level_sum,
    get_three_largest_basin_size_product,
)


def test_get_low_point_risk_level_sum():
    assert get_low_point_risk_level_sum(read_puzzle_input("test_input.txt")) == 15


def test_get_three_largest_basin_size_product():
    assert (
        get_three_largest_basin_size_product(read_puzzle_input("test_input.txt"))
        == 1134
    )
