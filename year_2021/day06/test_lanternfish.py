import pytest

from util import read_puzzle_input
from year_2021.day06.lanternfish import (
    get_num_lanternfish,
)


@pytest.mark.parametrize(
    "num_days,expected_output",
    [
        (0, 5),
        (18, 26),
        (80, 5934),
        (256, 26984457539),
    ],
)
def test_get_num_lanternfish(num_days, expected_output):
    assert (
        get_num_lanternfish(read_puzzle_input("test_input.txt"), num_days=num_days)
        == expected_output
    )
