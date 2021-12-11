from util import read_puzzle_input
from year_2021.day10.syntax_scoring import (
    get_syntax_error_score,
)


def test_get_syntax_error_score():
    assert get_syntax_error_score(read_puzzle_input("test_input.txt")) == 26397
