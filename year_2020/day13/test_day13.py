from year_2020.day13.shuttle_search import (
    get_bus_id_times_wait_time,
    get_earliest_bus_and_wait_time_for_airport,
)

TEST_INPUT = """
939
7,13,x,x,59,x,31,19
"""


def test_part_1():
    assert get_bus_id_times_wait_time(TEST_INPUT) == 295
    assert get_earliest_bus_and_wait_time_for_airport(TEST_INPUT) == (59, 5)
