import pytest

from util import read_puzzle_input
from year_2021.day14.extended_polymerization import (
    get_difference_most_least_common_element_counts,
)


@pytest.mark.parametrize(
    "num_steps,expected_output",
    [
        (10, 1588),
        (40, 2188189693529),
    ],
)
def test_get_difference_most_least_common_element_counts(num_steps, expected_output):
    assert (
        get_difference_most_least_common_element_counts(
            puzzle_input=read_puzzle_input("test_input.txt"),
            num_steps=num_steps,
        )
        == expected_output
    )
