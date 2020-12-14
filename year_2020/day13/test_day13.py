import pytest

from year_2020.day13.shuttle_search import (
    get_bus_id_times_wait_time,
    get_earliest_bus_and_wait_time_for_airport,
    get_shuttle_company_solution,
)

TEST_INPUT = """
939
7,13,x,x,59,x,31,19
"""

TEST_INPUT_2 = """
0
17,x,13,19
"""

TEST_INPUT_3 = """
0
67,7,59,61
"""

TEST_INPUT_4 = """
0
67,x,7,59,61
"""

TEST_INPUT_5 = """
0
67,7,x,59,61
"""

TEST_INPUT_6 = """
0
1789,37,47,1889
"""


def test_part_1():
    assert get_bus_id_times_wait_time(TEST_INPUT) == 295
    assert get_earliest_bus_and_wait_time_for_airport(TEST_INPUT) == (59, 5)


@pytest.mark.parametrize('test_input,expected', [
    (TEST_INPUT, 1068781),
    (TEST_INPUT_2, 3417),
    (TEST_INPUT_3, 754018),
    (TEST_INPUT_4, 779210),
    (TEST_INPUT_5, 1261476),
    (TEST_INPUT_6, 1202161486),
])
def test_part_2(test_input, expected):
    assert get_shuttle_company_solution(test_input) == expected
