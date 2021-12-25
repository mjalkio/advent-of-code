from util import read_puzzle_input
from year_2021.day25.sea_cucumber import (
    get_num_steps_no_movement,
)


def test_get_num_steps_no_movement():
    assert get_num_steps_no_movement(read_puzzle_input("test_input.txt")) == 58
