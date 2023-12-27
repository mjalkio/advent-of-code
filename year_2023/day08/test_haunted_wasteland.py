import pytest

from util import read_puzzle_input
from year_2023.day08.haunted_wasteland import (
    get_num_steps,
)


@pytest.mark.parametrize(
    "input_file, num_steps",
    [
        ("test_input.txt", 2),
        ("test_input_2.txt", 6),
    ],
)
def test_get_num_steps(input_file, num_steps):
    assert get_num_steps(read_puzzle_input(input_file)) == num_steps
