import pytest

from year_2020.day14.docking_data import (
    get_masked_value,
    get_memory_sum,
)


TEST_INPUT = """
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
"""


@pytest.mark.parametrize('value,expected', [(11, 73), (101, 101), (0, 64)])
def test_get_masked_value(value, expected):
    assert get_masked_value(value=value, mask='XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X') == expected


def test_get_memory_sum():
    assert get_memory_sum(TEST_INPUT) == 165
