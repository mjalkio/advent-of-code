from year_2020.day12.rain_risk import (
    get_manhattan_distance_after_navigation,
    get_navigation_destination,
    get_navigation_destination_with_waypoint,
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


def test_with_waypoint():
    assert get_navigation_destination_with_waypoint(TEST_INPUT) == (214, -72)
    assert get_manhattan_distance_after_navigation(TEST_INPUT, use_waypoint=True) == 286
