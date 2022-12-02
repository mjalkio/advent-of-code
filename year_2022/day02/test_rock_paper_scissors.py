from util import read_puzzle_input
from year_2022.day02.rock_paper_scissors import (
    get_correct_score,
    get_score,
)


def test_get_score():
    assert get_score(read_puzzle_input("test_input.txt")) == 15


def test_get_correct_score():
    assert get_correct_score(read_puzzle_input("test_input.txt")) == 12
