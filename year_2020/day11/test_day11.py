from year_2020.day11.seating_system import get_num_occupied_seats_at_convergence

TEST_INPUT = """
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
"""


def test_get_num_occupied_seats_at_convergence():
    assert get_num_occupied_seats_at_convergence(TEST_INPUT) == 37
