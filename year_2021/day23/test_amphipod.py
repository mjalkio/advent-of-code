from util import read_puzzle_input
from year_2021.day23.amphipod import (
    get_minimum_energy_required,
)


def test_get_minimum_energy_required():
    assert get_minimum_energy_required(read_puzzle_input("test_input.txt")) == 12521
