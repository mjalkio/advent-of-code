from util import read_puzzle_input
from year_2023.day07.camel_cards import (
    get_total_winnings,
)


def test_get_total_winnings():
    assert get_total_winnings(read_puzzle_input("test_input.txt")) == 6440
