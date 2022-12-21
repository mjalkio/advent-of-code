from util import read_puzzle_input
from year_2022.day21.monkey_math import (
    root_number,
)


def test_root_number():
    assert root_number(read_puzzle_input("test_input.txt")) == 152
