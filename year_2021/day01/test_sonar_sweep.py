from year_2021.day01.sonar_sweep import (
    count_depth_increases,
    count_sliding_window_depth_increases,
)

PUZZLE_INPUT = """
199
200
208
210
200
207
240
269
260
263
"""


def test_count_depth_increases():
    assert count_depth_increases(PUZZLE_INPUT) == 7


def test_count_sliding_window_depth_increases():
    assert count_sliding_window_depth_increases(PUZZLE_INPUT) == 5
