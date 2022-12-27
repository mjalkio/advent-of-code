from util import read_puzzle_input
from year_2022.day23.unstable_diffusion import (
    get_stable_round,
    num_empty_ground_tiles,
)


def test_num_empty_ground_tiles():
    assert num_empty_ground_tiles(read_puzzle_input("test_input.txt")) == 110


def test_get_stable_round():
    assert get_stable_round(read_puzzle_input("test_input.txt")) == 20
