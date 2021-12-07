from util import read_puzzle_input
from year_2021.day07.the_treachery_of_whales import (
    get_fuel_spent,
)


def test_get_fuel_spent():
    assert get_fuel_spent(read_puzzle_input('test_input.txt')) == 37
