import pytest

from day5part1 import num_jumps
from day5part2 import num_jumps_again


@pytest.fixture
def instructions():
    return [0, 3, 0, 1, -3]


def test_num_jumps(instructions):
    assert num_jumps(instructions) == 5


def test_num_jumps_again(instructions):
    assert num_jumps_again(instructions) == 10
