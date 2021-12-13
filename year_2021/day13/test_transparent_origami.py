from util import read_puzzle_input
from year_2021.day13.transparent_origami import (
    get_num_dots,
)


def test_get_num_dots():
    assert get_num_dots(read_puzzle_input("test_input.txt")) == 17
