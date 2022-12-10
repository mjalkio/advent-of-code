from util import read_puzzle_input
from year_2022.day09.rope_bridge import (
    num_positions_tail_visits,
)


def test_num_positions_tail_visits():
    assert num_positions_tail_visits(read_puzzle_input("test_input.txt")) == 13
