import pytest

from year_2020.day14.docking_data import (
    get_masked_address,
    get_masked_value,
    get_memory_sum,
)


TEST_INPUT = """
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
"""


TEST_INPUT_2 = """
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
"""


@pytest.mark.parametrize(
    'value,mask,expected',
    [
        (42, '000000000000000000000000000000X1001X', '000000000000000000000000000000X1101X'),
        (26, '00000000000000000000000000000000X0XX', '00000000000000000000000000000001X0XX'),
    ]
)
def test_get_masked_address(value, mask, expected):
    assert get_masked_address(value=value, mask=mask) == expected


@pytest.mark.parametrize('value,expected', [(11, 73), (101, 101), (0, 64)])
def test_get_masked_value(value, expected):
    assert get_masked_value(value=value, mask='XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X') == expected


def test_get_memory_sum():
    assert get_memory_sum(TEST_INPUT) == 165


def test_get_memory_sum_version_2():
    assert get_memory_sum(TEST_INPUT_2, use_version_2=True) == 208
