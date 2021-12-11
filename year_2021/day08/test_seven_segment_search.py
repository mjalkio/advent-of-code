from util import read_puzzle_input
from year_2021.day08.seven_segment_search import (
    get_num_easy_digit_outputs,
)


def test_get_num_easy_digit_outputs():
    assert get_num_easy_digit_outputs(read_puzzle_input('test_input.txt')) == 26
