from year_2020.day06.custom_customs import (
    num_questions_answered_by_group,
    sum_questions_answered_by_group,
)

TEST_CASE_1 = """
abcx
abcy
abcz
"""

TEST_INPUT_1 = """
abc

a
b
c

ab
ac

a
a
a
a

b
"""


def test_num_questions_answered_by_group():
    assert num_questions_answered_by_group(TEST_CASE_1) == 6


def test_sum_questions_answered_by_group():
    assert sum_questions_answered_by_group(TEST_INPUT_1) == 11
