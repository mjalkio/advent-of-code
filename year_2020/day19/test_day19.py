import pytest

from year_2020.day19.monster_messages import does_message_match_rules, get_valid_messages

TEST_RULES_1 = """
0: 1 2
1: "a"
2: 1 3 | 3 1
3: "b"
"""

TEST_RULES_2 = """
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"
"""


@pytest.mark.parametrize(
    'rules, rule_num, valid_messages',
    [
        (TEST_RULES_1, 0, {'aab', 'aba'}),
        (TEST_RULES_1, 1, {'a'}),
        (TEST_RULES_1, 2, {'ab', 'ba'}),
        (TEST_RULES_1, 3, {'b'}),
        (
            TEST_RULES_2,
            0,
            {'aaaabb', 'aaabab', 'abbabb', 'abbbab', 'aabaab', 'aabbbb', 'abaaab', 'ababbb'}
        ),
        (TEST_RULES_2, 1, {'aaab', 'aaba', 'bbab', 'bbba', 'abaa', 'abbb', 'baaa', 'babb'}),
        (TEST_RULES_2, 2, {'aa', 'bb'}),
        (TEST_RULES_2, 3, {'ab', 'ba'}),
        (TEST_RULES_2, 4, {'a'}),
        (TEST_RULES_2, 5, {'b'}),
    ]
)
def test_get_valid_messages(rules, rule_num, valid_messages):
    assert get_valid_messages(rules).get(rule_num) == valid_messages


@pytest.mark.parametrize(
    'rules, rule_num, message, expected',
    [
        (TEST_RULES_2, 0, 'ababbb', True),
        (TEST_RULES_2, 0, 'abbbab', True),
        (TEST_RULES_2, 0, 'bababa', False),
        (TEST_RULES_2, 0, 'aaabbb', False),
        (TEST_RULES_2, 0, 'aaaabbb', False),
    ]
)
def test_does_message_match_rule(rules, rule_num, message, expected):
    assert does_message_match_rules(rules, rule_num, message) == expected
