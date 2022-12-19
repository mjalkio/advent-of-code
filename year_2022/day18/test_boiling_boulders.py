from util import read_puzzle_input
from year_2022.day18.boiling_boulders import (
    approximate_surface_area,
)


def test_surface_area():
    assert approximate_surface_area(read_puzzle_input("test_input.txt")) == 64
