from util import read_puzzle_input
from year_2022.day12.hill_climbing_algorithm import (
    fewest_steps,
    fewest_steps_possible,
)


def test_fewest_steps():
    assert fewest_steps(read_puzzle_input("test_input.txt")) == 31


def test_fewest_steps_possible():
    assert fewest_steps_possible(read_puzzle_input("test_input.txt")) == 29
