import pytest

from day6part1 import num_cycles


@pytest.fixture
def memory_banks():
    return [0, 3, 0, 1, -3]


def test_num_cycles(memory_banks):
    assert num_cycles(memory_banks) == 5
