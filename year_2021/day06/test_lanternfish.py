from util import read_puzzle_input
from year_2021.day06.lanternfish import (
    get_num_lanternfish,
)


def test_get_num_lanternfish():
    assert get_num_lanternfish(read_puzzle_input('test_input.txt'), num_days=0) == 5
    assert get_num_lanternfish(read_puzzle_input('test_input.txt'), num_days=18) == 26
    assert get_num_lanternfish(read_puzzle_input('test_input.txt'), num_days=80) == 5934
    assert get_num_lanternfish(read_puzzle_input('test_input.txt'), num_days=256) == 26984457539
