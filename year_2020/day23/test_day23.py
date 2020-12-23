import pytest

from year_2020.day23.crab_cups import get_crab_cups

TEST_INPUT = '389125467'


@pytest.mark.parametrize('num_moves, expected', [(10, '92658374'), (100, '67384529')])
def test_get_crap_cups(num_moves, expected):
    assert get_crab_cups(TEST_INPUT, num_moves=num_moves) == expected


def test_get_crap_cups_part_two():
    assert get_crab_cups(TEST_INPUT, num_moves=10000000, is_part_two=True) == 149245887792
