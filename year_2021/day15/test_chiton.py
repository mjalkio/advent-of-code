from util import read_puzzle_input
from year_2021.day15.chiton import (
    get_lowest_risk_path_risk,
)


def test_get_lowest_risk_path_risk():
    assert get_lowest_risk_path_risk(read_puzzle_input("test_input.txt")) == 40


def test_get_lowest_risk_path_risk_full_map():
    assert (
        get_lowest_risk_path_risk(
            read_puzzle_input("test_input.txt"), use_full_map=True
        )
        == 315
    )
