from util import read_puzzle_input
from year_2021.day14.extended_polymerization import (
    get_difference_most_least_common_element_counts,
)


def test_get_difference_most_least_common_element_counts():
    assert (
        get_difference_most_least_common_element_counts(
            read_puzzle_input("test_input.txt")
        )
        == 1588
    )
