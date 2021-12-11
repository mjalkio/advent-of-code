from year_2020.day11.seating_system import (
    get_num_occupied_seats_at_convergence,
    get_surrounding_chairs_part_2,
)

TEST_INPUT = """
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""


def test_get_num_occupied_seats_at_convergence():
    assert get_num_occupied_seats_at_convergence(TEST_INPUT) == 37


def test_get_num_occupied_seats_at_convergence_part_2():
    assert (
        get_num_occupied_seats_at_convergence(
            puzzle_input=TEST_INPUT,
            surrounding_chair_fn=get_surrounding_chairs_part_2,
            max_surrounding_occupied=5,
        )
        == 26
    )
