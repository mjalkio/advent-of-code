from util import read_puzzle_input
from year_2021.day18.snailfish import (
    do_homework,
)


def test_get_magnitude():
    assert do_homework(read_puzzle_input("test_input.txt")) == 4140
