from util import read_puzzle_input
from year_2021.day11.dumbo_octopus import (
    get_num_flashes,
)


def test_get_num_flashes():
    assert get_num_flashes(read_puzzle_input("test_input.txt")) == 1656
