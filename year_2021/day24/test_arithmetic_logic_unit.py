import pytest

from util import read_puzzle_input
from year_2021.day24.arithmetic_logic_unit import run_program, w, x, y, z


@pytest.mark.parametrize(
    "inputs,expected_output",
    [
        (
            [-3],
            {
                w: 0,
                x: 3,
                y: 0,
                z: 0,
            },
        ),
        (
            [10],
            {
                w: 0,
                x: -10,
                y: 0,
                z: 0,
            },
        ),
    ],
)
def test_run_program(inputs, expected_output):
    assert run_program(read_puzzle_input("test_negate.txt"), inputs) == expected_output
