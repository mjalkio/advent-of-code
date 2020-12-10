from year_2020.day10.adapter_array import get_joltage_difference_counts

TEST_INPUT_1 = """
16
10
15
5
1
11
7
19
6
12
4
"""

TEST_INPUT_2 = """
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""


def test_get_joltage_difference_counts():
    assert get_joltage_difference_counts(TEST_INPUT_1) == (7, 0, 5)
    assert get_joltage_difference_counts(TEST_INPUT_2) == (22, 0, 10)
