from util import read_puzzle_input
from year_2021.day05.hydrothermal_venture import (
    get_num_dangerous_points,
)


def test_get_num_dangerous_points():
    assert get_num_dangerous_points(read_puzzle_input('test_input.txt')) == 5
