from util import read_puzzle_input
from year_2021.day04.giant_squid import (
    get_losing_board_score,
    get_winning_board_score,
)


def test_get_winning_board_score():
    assert get_winning_board_score(read_puzzle_input("test_input.txt")) == 4512


def test_get_losing_board_score():
    assert get_losing_board_score(read_puzzle_input("test_input.txt")) == 1924
