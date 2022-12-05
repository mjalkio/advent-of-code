import pytest

from util import read_puzzle_input
from year_2022.day05.supply_stacks import (
    get_top_crates,
)


@pytest.mark.parametrize(
    "cratemover_model,top_crates",
    [("9000", "CMZ"), ("9001", "MCD")],
)
def test_get_top_crates(cratemover_model, top_crates):
    assert (
        get_top_crates(
            read_puzzle_input("test_input.txt"), cratemover_model=cratemover_model
        )
        == top_crates
    )
