import pytest

from util import read_puzzle_input
from year_2021.day19.beacon_scanner import (
    get_num_beacons,
)


@pytest.mark.xfail
def test_get_num_beacons():
    assert get_num_beacons(read_puzzle_input("test_input.txt")) == 79
