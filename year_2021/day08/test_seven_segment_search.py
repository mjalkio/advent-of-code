from util import read_puzzle_input
from year_2021.day08.seven_segment_search import (
    get_num_easy_digit_outputs,
    get_outputs_sum,
)


def test_get_num_easy_digit_outputs():
    assert get_num_easy_digit_outputs(read_puzzle_input("test_input.txt")) == 26


def test_get_outputs_sum():
    assert get_outputs_sum(read_puzzle_input("test_input.txt")) == 61229
