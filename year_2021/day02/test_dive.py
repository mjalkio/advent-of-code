from year_2021.day02.dive import (
    get_position_product,
)

PUZZLE_INPUT = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""


def test_get_position_product():
    assert get_position_product(PUZZLE_INPUT) == 150
