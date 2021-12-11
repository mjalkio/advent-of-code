from util import read_puzzle_input
from year_2021.day05.hydrothermal_venture import (
    get_num_dangerous_points,
)


def test_get_num_dangerous_points():
    puzzle_input = read_puzzle_input("test_input.txt")
    assert get_num_dangerous_points(puzzle_input) == 5
    assert get_num_dangerous_points(puzzle_input, use_diagonal_lines=True) == 12
