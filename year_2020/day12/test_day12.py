from year_2020.day12.rain_risk import (
    get_manhattan_distance_after_navigation,
    get_navigation_destination,
)


TEST_INPUT = """
F10
N3
F7
R90
F11
"""


def test_get_manhattan_distance_after_navigation():
    assert get_manhattan_distance_after_navigation(TEST_INPUT) == 25


def test_get_navigation_destination():
    assert get_navigation_destination(TEST_INPUT) == (17, -8)
