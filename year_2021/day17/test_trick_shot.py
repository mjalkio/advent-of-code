from util import read_puzzle_input
from year_2021.day17.trick_shot import (
    get_highest_possible_y_position,
)


def test_get_highest_possible_y_position():
    assert get_highest_possible_y_position(read_puzzle_input("test_input.txt")) == 45
