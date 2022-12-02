from util import read_puzzle_input
from year_2022.day01.calorie_counting import (
    get_max_total_calories,
    get_top_three_total_calories,
)


def test_get_max_total_calories():
    assert get_max_total_calories(read_puzzle_input("test_input.txt")) == 24000


def test_get_top_three_total_calories():
    assert get_top_three_total_calories(read_puzzle_input("test_input.txt")) == 45000
