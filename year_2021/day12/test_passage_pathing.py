import pytest

from util import read_puzzle_input
from year_2021.day12.passage_pathing import (
    get_num_paths,
)


@pytest.mark.parametrize(
    "input_file,expected_output",
    [
        ("test_input.txt", 10),
        ("test_input2.txt", 19),
        ("test_input3.txt", 226),
    ],
)
def test_get_num_paths(input_file, expected_output):
    assert get_num_paths(read_puzzle_input(input_file)) == expected_output
