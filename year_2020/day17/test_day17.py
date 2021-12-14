import pytest

from year_2020.day17.conway_cubes import get_num_active_cubes, get_num_active_cubes_4d

TEST_INPUT = """
.#.
..#
###
"""


def test_get_num_active_cubes():
    assert get_num_active_cubes(TEST_INPUT) == 112


@pytest.mark.slow
def test_get_num_active_cubes_4d():
    assert get_num_active_cubes_4d(TEST_INPUT) == 848
