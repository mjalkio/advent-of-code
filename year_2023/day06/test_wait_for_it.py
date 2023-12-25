from util import read_puzzle_input
from year_2023.day06.wait_for_it import (
    get_product_num_ways_beat_record,
)


def test_get_product_num_ways_beat_record():
    assert get_product_num_ways_beat_record(read_puzzle_input("test_input.txt")) == 288
