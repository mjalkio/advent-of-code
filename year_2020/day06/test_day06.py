from year_2020.day06.custom_customs import sum_questions_answered_by_group

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


def test_sum_questions_answered_by_group():
    assert sum_questions_answered_by_group(TEST_INPUT_1) == 11
