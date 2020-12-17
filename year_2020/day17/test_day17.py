from year_2020.day17.conway_cubes import get_num_active_cubes

TEST_INPUT = """
.#.
..#
###
"""


def test_get_num_active_cubes():
    assert get_num_active_cubes(TEST_INPUT) == 112
