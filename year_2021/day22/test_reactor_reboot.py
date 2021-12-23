import pytest

from util import read_puzzle_input
from year_2021.day22.reactor_reboot import (
    get_num_cubes_on,
)


@pytest.mark.parametrize(
    "input_file,is_initialization_procedure,expected_output",
    [
        # ("test_input.txt", True, 39),
        # ("test_input_2.txt", True, 590784),
        # ("test_input_3.txt", True, 474140),
        ("test_approach_1.txt", True, 46),
        # ("test_input_3.txt", False, 2758514936282235),
    ],
)
def test_get_num_cubes_on(input_file, is_initialization_procedure, expected_output):
    assert (
        get_num_cubes_on(read_puzzle_input(input_file), is_initialization_procedure)
        == expected_output
    )
