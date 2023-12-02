from util import read_puzzle_input
from year_2023.day02.cube_conundrum import (
    sum_min_set_powers,
    sum_possible_games,
)


def test_sum_possible_games():
    assert sum_possible_games(read_puzzle_input("test_input.txt")) == 8


def test_sum_min_set_powers():
    assert sum_min_set_powers(read_puzzle_input("test_input.txt")) == 2286
