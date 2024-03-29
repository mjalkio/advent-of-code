import pytest

from util import read_puzzle_input
from year_2022.day19.not_enough_minerals import (
    geode_count_product,
    sum_quality_levels,
)


@pytest.mark.slow
def test_sum_quality_levels():
    assert sum_quality_levels(read_puzzle_input("test_input.txt")) == 33


@pytest.mark.slow
def test_geode_count_product():
    assert geode_count_product(read_puzzle_input("test_input.txt")) == 56 * 62
