from util import read_puzzle_input
from year_2022.day05.supply_stacks import (
    get_top_crates,
)


def test_get_top_crates():
    assert get_top_crates(read_puzzle_input("test_input.txt")) == "CMZ"
