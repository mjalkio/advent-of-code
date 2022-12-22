from util import read_puzzle_input
from year_2022.day22.monkey_map import (
    final_password,
)


def test_final_password():
    assert final_password(read_puzzle_input("test_input.txt")) == 6032
