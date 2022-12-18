from util import read_puzzle_input
from year_2022.day15.beacon_exclusion_zone import (
    num_positions_cannot_contain_beacon,
)


def test_num_positions_cannot_contain_beacon():
    assert (
        num_positions_cannot_contain_beacon(
            read_puzzle_input("test_input.txt"), row_num=10
        )
        == 26
    )
