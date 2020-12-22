from year_2020.day22.crab_combat import get_winning_combat_score

TEST_INPUT = """
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
"""

LOOP_FOREVER_INPUT = """
Player 1:
43
19

Player 2:
2
29
14
"""


def test_get_winning_combat_score():
    assert get_winning_combat_score(TEST_INPUT) == 306


def test_get_winning_combat_score_recursive():
    assert get_winning_combat_score(TEST_INPUT, recursive=True) == 291


def test_does_not_loop_forever():
    assert get_winning_combat_score(LOOP_FOREVER_INPUT, recursive=True) is not None
