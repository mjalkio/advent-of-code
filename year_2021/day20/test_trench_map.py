import pytest

from util import read_puzzle_input
from year_2021.day20.trench_map import (
    get_num_lit_pixels,
)


@pytest.mark.parametrize(
    "num_enhancements,expected_output",
    [
        (2, 35),
        pytest.param(50, 3351, marks=pytest.mark.slow),
    ],
)
def test_get_num_lit_pixels(num_enhancements, expected_output):
    assert (
        get_num_lit_pixels(
            read_puzzle_input("test_input.txt"), num_enhancements=num_enhancements
        )
        == expected_output
    )
