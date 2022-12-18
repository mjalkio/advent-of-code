import pytest

from util import read_puzzle_input
from year_2022.day13.distress_signal import (
    decoder_key,
    is_ordered,
    sum_indices_ordered_pairs,
)


@pytest.mark.parametrize(
    "left, right, expected",
    [
        ("[1,1,3,1,1]", "[1,1,5,1,1]", True),
        ("[[1],[2,3,4]]", "[[1],4]", True),
        ("[9]", "[[8,7,6]]", False),
        ("[[4,4],4,4]", "[[4,4],4,4,4]", True),
        ("[7,7,7,7]", "[7,7,7]", False),
        ("[]", "[3]", True),
        ("[[[]]]", "[[]]", False),
        ("[1,[2,[3,[4,[5,6,7]]]],8,9]", "[1,[2,[3,[4,[5,6,0]]]],8,9]", False),
    ],
)
def test_is_ordered(left, right, expected):
    assert is_ordered(left, right) == expected


def test_sum_indices_ordered_pairs():
    assert sum_indices_ordered_pairs(read_puzzle_input("test_input.txt")) == 13


def test_decoder_key():
    assert decoder_key(read_puzzle_input("test_input.txt")) == 140
