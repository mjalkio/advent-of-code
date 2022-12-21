from util import read_puzzle_input
from year_2022.day21.monkey_math import (
    human_number,
    root_number,
)


def test_root_number():
    assert root_number(read_puzzle_input("test_input.txt")) == 152


def test_human_number():
    assert human_number(read_puzzle_input("test_input.txt")) == 301
