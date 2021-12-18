from util import read_puzzle_input
from year_2021.day17.trick_shot import (
    get_highest_possible_y_position,
    get_num_valid_initial_velocities,
)


def test_get_highest_possible_y_position():
    assert get_highest_possible_y_position(read_puzzle_input("test_input.txt")) == 45


def test_get_num_valid_initial_velocities():
    assert get_num_valid_initial_velocities(read_puzzle_input("test_input.txt")) == 112
