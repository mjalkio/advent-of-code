from util import read_puzzle_input
from year_2022.day18.boiling_boulders import (
    approximate_surface_area,
    exterior_surface_area,
)


def test_approximate_surface_area():
    assert approximate_surface_area(read_puzzle_input("test_input.txt")) == 64


def test_exterior_surface_area():
    assert exterior_surface_area(read_puzzle_input("test_input.txt")) == 58
