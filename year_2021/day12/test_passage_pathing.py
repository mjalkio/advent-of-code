import pytest

from util import read_puzzle_input
from year_2021.day12.passage_pathing import (
    get_num_paths,
)


@pytest.mark.parametrize(
    "input_file,expected_output,max_small_cave_visits",
    [
        ("test_input.txt", 10, 1),
        ("test_input2.txt", 19, 1),
        ("test_input3.txt", 226, 1),
        ("test_input.txt", 36, 2),
        ("test_input2.txt", 103, 2),
        ("test_input3.txt", 3509, 2),
    ],
)
def test_get_num_paths(input_file, expected_output, max_small_cave_visits):
    assert (
        get_num_paths(read_puzzle_input(input_file), max_small_cave_visits)
        == expected_output
    )
