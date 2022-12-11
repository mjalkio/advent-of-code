import pytest

from util import read_puzzle_input
from year_2022.day11.monkey_in_the_middle import (
    get_monkey_business,
)


@pytest.mark.parametrize(
    "num_rounds,very_worried,expected", [(20, False, 10605), (10_000, True, 2713310158)]
)
def test_get_monkey_business(num_rounds, very_worried, expected):
    assert (
        get_monkey_business(
            read_puzzle_input("test_input.txt"),
            num_rounds=num_rounds,
            very_worried=very_worried,
        )
        == expected
    )
