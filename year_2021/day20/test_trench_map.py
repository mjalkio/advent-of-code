from util import read_puzzle_input
from year_2021.day20.trench_map import (
    get_num_lit_pixels,
)


def test_get_num_lit_pixels():
    assert get_num_lit_pixels(read_puzzle_input("test_input.txt")) == 35
