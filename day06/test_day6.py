import pytest

from day6part1 import num_cycles


@pytest.fixture
def initial_config():
    return [0, 2, 7, 0]


def test_num_cycles(initial_config):
    assert num_cycles(initial_config) == 5
