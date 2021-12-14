from util import read_puzzle_input
from year_2019.day01.the_tyranny_of_the_rocket_equation import (
    get_total_fuel_required,
    get_total_fuel_required_double_check,
)


def test_get_total_fuel_required():
    assert (
        get_total_fuel_required(read_puzzle_input("test_input.txt"))
        == 2 + 2 + 654 + 33583
    )


def test_get_total_fuel_required_double_check():
    assert (
        get_total_fuel_required_double_check(read_puzzle_input("test_input.txt"))
        == 2 + 2 + 966 + 50346
    )
