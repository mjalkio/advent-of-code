from util import read_puzzle_input
from year_2021.day07.the_treachery_of_whales import (
    get_fuel_spent,
    get_fuel_spent_part_two,
)


def test_get_fuel_spent():
    assert get_fuel_spent(read_puzzle_input("test_input.txt")) == 37


def test_get_fuel_spent_part_two():
    assert get_fuel_spent_part_two(read_puzzle_input("test_input.txt")) == 168
