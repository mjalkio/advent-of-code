import pytest

from util import read_puzzle_input
from year_2021.day16.packet_decoder import (
    get_version_sum,
)


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("test_input1.txt", 16),
        ("test_input1.txt", 12),
        ("test_input1.txt", 23),
        ("test_input1.txt", 31),
    ],
)
def test_get_version_sum(test_input, expected):
    assert get_version_sum(read_puzzle_input(test_input)) == expected
