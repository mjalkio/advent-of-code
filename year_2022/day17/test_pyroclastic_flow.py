from util import read_puzzle_input
from year_2022.day17.pyroclastic_flow import (
    rock_tower_height,
)


def test_rock_tower_height():
    assert rock_tower_height(read_puzzle_input("test_input.txt")) == 3068
