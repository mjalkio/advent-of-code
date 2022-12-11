from util import read_puzzle_input
from year_2022.day11.monkey_in_the_middle import (
    get_monkey_business,
)


def test_get_monkey_business():
    assert get_monkey_business(read_puzzle_input("test_input.txt")) == 10605
