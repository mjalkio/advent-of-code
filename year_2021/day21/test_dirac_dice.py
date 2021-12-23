import pytest

from util import read_puzzle_input
from year_2021.day21.dirac_dice import (
    get_losing_score_times_num_rolls,
    get_num_universes,
)


def test_get_losing_score_times_num_rolls():
    assert (
        get_losing_score_times_num_rolls(read_puzzle_input("test_input.txt")) == 739785
    )


@pytest.mark.slow
def test_get_num_universes():
    assert get_num_universes(read_puzzle_input("test_input.txt")) == 444356092776315
