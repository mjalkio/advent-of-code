from util import read_puzzle_input
from year_2022.day15.beacon_exclusion_zone import (
    distress_beacon_tuning_frequency,
    num_positions_cannot_contain_beacon,
)


def test_num_positions_cannot_contain_beacon():
    assert (
        num_positions_cannot_contain_beacon(
            read_puzzle_input("test_input.txt"), row_num=10
        )
        == 26
    )


def test_distress_beacon_tuning_frequency():
    assert (
        distress_beacon_tuning_frequency(
            read_puzzle_input("test_input.txt"), max_coord=20
        )
        == 56000011
    )
