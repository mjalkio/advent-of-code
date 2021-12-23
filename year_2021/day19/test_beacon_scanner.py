import pytest

from util import read_puzzle_input
from year_2021.day19.beacon_scanner import (
    get_max_scanner_distance,
    get_num_beacons,
)


@pytest.mark.slow
def test_get_num_beacons():
    assert get_num_beacons(read_puzzle_input("test_input.txt")) == 79


@pytest.mark.slow
def test_get_max_scanner_distance():
    assert get_max_scanner_distance(read_puzzle_input("test_input.txt")) == 3621
