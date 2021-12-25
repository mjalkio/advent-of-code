import pytest

from util import read_puzzle_input
from year_2021.day22.reactor_reboot import (
    get_num_cubes_on,
)


@pytest.mark.parametrize(
    "input_file,is_initialization_procedure,expected_output",
    [
        ("test_input.txt", True, 39),
        ("test_input_2.txt", True, 590784),
        ("test_input_3.txt", True, 474140),
        ("test_approach_1.txt", True, 27 + 19),
        ("test_approach_2.txt", True, 27 + 19),
        ("test_approach_3.txt", True, 27 + 19 - 8),
        ("test_approach_4.txt", True, 30),
        ("test_approach_5.txt", True, 26),
        ("test_approach_6.txt", True, 26),
        ("test_approach_7.txt", True, 18),
        ("test_approach_8.txt", True, 26),
        ("test_input_3.txt", False, 2758514936282235),
    ],
)
def test_get_num_cubes_on(input_file, is_initialization_procedure, expected_output):
    assert (
        get_num_cubes_on(read_puzzle_input(input_file), is_initialization_procedure)
        == expected_output
    )
