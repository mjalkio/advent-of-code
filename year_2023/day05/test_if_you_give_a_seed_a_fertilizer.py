from util import read_puzzle_input
from year_2023.day05.if_you_give_a_seed_a_fertilizer import (
    get_lowest_location_number,
)


def test_get_lowest_location_number():
    assert get_lowest_location_number(read_puzzle_input("test_input.txt")) == 35


def test_get_lowest_location_number_part_2():
    assert (
        get_lowest_location_number(read_puzzle_input("test_input.txt"), use_ranges=True)
        == 46
    )
