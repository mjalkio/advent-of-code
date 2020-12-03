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
    assert num_trees_hit(tree_map=TEST_INPUT_1, horizontal_change=3, vertical_change=1) == 7
