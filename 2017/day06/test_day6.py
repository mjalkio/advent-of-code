import pytest

from day6part1 import num_cycles
from day6part2 import loop_size


@pytest.fixture
def initial_config():
    return [0, 2, 7, 0]


def test_num_cycles(initial_config):
    assert num_cycles(initial_config) == 5


def test_loop_size(initial_config):
    assert loop_size(initial_config) == 4
