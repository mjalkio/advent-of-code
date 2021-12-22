import pytest

from util import read_puzzle_input
from year_2021.day22.reactor_reboot import (
    get_num_cubes_on,
)


@pytest.mark.parametrize(
    "input_file,expected_output",
    [
        ("test_input.txt", 39),
        ("test_input_2.txt", 590784),
    ],
)
def test_get_num_cubes_on(input_file, expected_output):
    assert get_num_cubes_on(read_puzzle_input(input_file)) == expected_output
