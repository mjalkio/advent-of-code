import pytest

from util import read_puzzle_input
from year_2022.day09.rope_bridge import (
    num_positions_tail_visits,
)


@pytest.mark.parametrize(
    "file_name,num_knots,expected_output",
    [
        ("test_input.txt", 2, 13),
        ("test_input.txt", 10, 1),
        ("test_input_2.txt", 10, 36),
    ],
)
def test_num_positions_tail_visits(file_name, num_knots, expected_output):
    assert (
        num_positions_tail_visits(read_puzzle_input(file_name), num_knots=num_knots)
        == expected_output
    )
