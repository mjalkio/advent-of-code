from util import read_puzzle_input
from year_2021.day03.binary_diagnostic import (
    get_power_consumption,
)


def test_get_power_consumption():
    assert get_power_consumption(read_puzzle_input('test_input.txt')) == 198
