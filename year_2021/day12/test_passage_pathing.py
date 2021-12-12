import pytest

from util import read_puzzle_input
from year_2021.day12.passage_pathing import (
    get_num_paths,
)


@pytest.mark.parametrize(
    "input_file,expected_output,can_revisit_single_small_cave",
    [
        ("test_input.txt", 10, False),
        ("test_input2.txt", 19, False),
        ("test_input3.txt", 226, False),
        ("test_input.txt", 36, True),
        ("test_input2.txt", 103, True),
        ("test_input3.txt", 3509, True),
    ],
)
def test_get_num_paths(input_file, expected_output, can_revisit_single_small_cave):
    assert (
        get_num_paths(read_puzzle_input(input_file), can_revisit_single_small_cave)
        == expected_output
    )
