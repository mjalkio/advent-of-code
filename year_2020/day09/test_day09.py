import pytest

from year_2020.day09.encoding_error import (
    encryption_weakness,
    first_invalid_number,
    has_pair_that_sums,
)

EXAMPLE_1_PREAMBLE = range(1, 26)
EXAMPLE_2_PREAMBLE = list(range(1, 20)) + list(range(21, 26)) + [45]


TEST_INPUT = """
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
"""


@pytest.mark.parametrize(
    'number,preamble,expected',
    [
        (26, EXAMPLE_1_PREAMBLE, True),
        (49, EXAMPLE_1_PREAMBLE, True),
        (100, EXAMPLE_1_PREAMBLE, False),
        (50, EXAMPLE_1_PREAMBLE, False),
        (26, EXAMPLE_2_PREAMBLE, True),
        (65, EXAMPLE_2_PREAMBLE, False),
        (64, EXAMPLE_2_PREAMBLE, True),
        (66, EXAMPLE_2_PREAMBLE, True),
    ]
)
def test_has_pair_that_sums(number, preamble, expected):
    assert has_pair_that_sums(number, preamble) == expected


def test_first_invalid_number():
    assert first_invalid_number(TEST_INPUT, preamble_size=5) == 127


def test_encryption_weakness():
    assert encryption_weakness(TEST_INPUT, preamble_size=5) == 62
