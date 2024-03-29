from util import read_puzzle_input
from year_2023.day04.scratchcards import (
    get_num_scratchcards,
    get_point_value,
)


def test_get_point_value():
    assert get_point_value(read_puzzle_input("test_input.txt")) == 13


def test_get_num_scratchcards():
    assert get_num_scratchcards(read_puzzle_input("test_input.txt")) == 30
