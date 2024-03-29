import pytest

from util import read_puzzle_input
from year_2019.day03.crossed_wires import (
    get_distance_closest_intersection,
    get_fewest_combined_steps,
)


@pytest.mark.parametrize(
    "input_file,expected_output",
    [("test_input.txt", 6), ("test_input2.txt", 159), ("test_input3.txt", 135)],
)
def test_get_distance_closest_intersection(input_file, expected_output):
    assert (
        get_distance_closest_intersection(read_puzzle_input(input_file))
        == expected_output
    )


@pytest.mark.parametrize(
    "input_file,expected_output",
    [("test_input.txt", 30), ("test_input2.txt", 610), ("test_input3.txt", 410)],
)
def test_get_fewest_combined_steps(input_file, expected_output):
    assert get_fewest_combined_steps(read_puzzle_input(input_file)) == expected_output
