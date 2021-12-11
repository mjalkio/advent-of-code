import pytest

from year_2020.day03.toboggan_trajectory import num_trees_hit

TEST_INPUT_1 = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""


def test_part_1():
    assert (
        num_trees_hit(tree_map=TEST_INPUT_1, horizontal_change=3, vertical_change=1)
        == 7
    )


@pytest.mark.parametrize(
    "horizontal_change,vertical_change,expected",
    [
        (1, 1, 2),
        (3, 1, 7),
        (5, 1, 3),
        (7, 1, 4),
        (1, 2, 2),
    ],
)
def test_part_2(horizontal_change, vertical_change, expected):
    assert (
        num_trees_hit(
            tree_map=TEST_INPUT_1,
            horizontal_change=horizontal_change,
            vertical_change=vertical_change,
        )
        == expected
    )
