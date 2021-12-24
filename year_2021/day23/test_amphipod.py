import pytest

from util import read_puzzle_input
from year_2021.day23.amphipod import (
    get_minimum_energy_required,
)


@pytest.mark.parametrize(
    "input_file,expected_output",
    [("test_input.txt", 12521), ("test_input_2.txt", 44169)],
)
def test_get_minimum_energy_required(input_file, expected_output):
    assert get_minimum_energy_required(read_puzzle_input(input_file)) == expected_output
