import pytest

from year_2020.day19.monster_messages import (
    does_message_match_rules,
    get_valid_messages,
)

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

TEST_RULES_3 = """
42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1
"""

TEST_RULES_4 = """
42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31 | 42 11 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42 | 42 8
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1
"""


@pytest.mark.parametrize(
    "rules, rule_num, valid_messages",
    [
        (TEST_RULES_1, 0, {"aab", "aba"}),
        (TEST_RULES_1, 1, {"a"}),
        (TEST_RULES_1, 2, {"ab", "ba"}),
        (TEST_RULES_1, 3, {"b"}),
        (
            TEST_RULES_2,
            0,
            {
                "aaaabb",
                "aaabab",
                "abbabb",
                "abbbab",
                "aabaab",
                "aabbbb",
                "abaaab",
                "ababbb",
            },
        ),
        (
            TEST_RULES_2,
            1,
            {"aaab", "aaba", "bbab", "bbba", "abaa", "abbb", "baaa", "babb"},
        ),
        (TEST_RULES_2, 2, {"aa", "bb"}),
        (TEST_RULES_2, 3, {"ab", "ba"}),
        (TEST_RULES_2, 4, {"a"}),
        (TEST_RULES_2, 5, {"b"}),
    ],
)
def test_get_valid_messages(rules, rule_num, valid_messages):
    assert get_valid_messages(rules).get(rule_num) == valid_messages


@pytest.mark.parametrize(
    "rules, rule_num, message, expected",
    [
        (TEST_RULES_2, 0, "ababbb", True),
        (TEST_RULES_2, 0, "abbbab", True),
        (TEST_RULES_2, 0, "bababa", False),
        (TEST_RULES_2, 0, "aaabbb", False),
        (TEST_RULES_2, 0, "aaaabbb", False),
        (TEST_RULES_3, 0, "abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa", False),
        (TEST_RULES_3, 0, "bbabbbbaabaabba", True),
        (TEST_RULES_3, 0, "babbbbaabbbbbabbbbbbaabaaabaaa", False),
        (TEST_RULES_3, 0, "aaabbbbbbaaaabaababaabababbabaaabbababababaaa", False),
        (TEST_RULES_3, 0, "bbbbbbbaaaabbbbaaabbabaaa", False),
        (TEST_RULES_3, 0, "bbbababbbbaaaaaaaabbababaaababaabab", False),
        (TEST_RULES_3, 0, "ababaaaaaabaaab", True),
        (TEST_RULES_3, 0, "ababaaaaabbbaba", True),
        (TEST_RULES_3, 0, "baabbaaaabbaaaababbaababb", False),
        (TEST_RULES_3, 0, "abbbbabbbbaaaababbbbbbaaaababb", False),
        (TEST_RULES_3, 0, "aaaaabbaabaaaaababaa", False),
        (TEST_RULES_3, 0, "aaaabbaaaabbaaa", False),
        (TEST_RULES_3, 0, "aaaabbaabbaaaaaaabbbabbbaaabbaabaaa", False),
        (TEST_RULES_3, 0, "babaaabbbaaabaababbaabababaaab", False),
        (TEST_RULES_3, 0, "aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba", False),
        (TEST_RULES_4, 0, "abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa", False),
        (TEST_RULES_4, 0, "bbabbbbaabaabba", True),
        (TEST_RULES_4, 0, "babbbbaabbbbbabbbbbbaabaaabaaa", True),
        (TEST_RULES_4, 0, "aaabbbbbbaaaabaababaabababbabaaabbababababaaa", True),
        (TEST_RULES_4, 0, "bbbbbbbaaaabbbbaaabbabaaa", True),
        (TEST_RULES_4, 0, "bbbababbbbaaaaaaaabbababaaababaabab", True),
        (TEST_RULES_4, 0, "ababaaaaaabaaab", True),
        (TEST_RULES_4, 0, "ababaaaaabbbaba", True),
        (TEST_RULES_4, 0, "baabbaaaabbaaaababbaababb", True),
        (TEST_RULES_4, 0, "abbbbabbbbaaaababbbbbbaaaababb", True),
        (TEST_RULES_4, 0, "aaaaabbaabaaaaababaa", True),
        (TEST_RULES_4, 0, "aaaabbaaaabbaaa", False),
        (TEST_RULES_4, 0, "aaaabbaabbaaaaaaabbbabbbaaabbaabaaa", True),
        (TEST_RULES_4, 0, "babaaabbbaaabaababbaabababaaab", False),
        (TEST_RULES_4, 0, "aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba", True),
    ],
)
def test_does_message_match_rule(rules, rule_num, message, expected):
    assert does_message_match_rules(rules, rule_num, message) == expected
