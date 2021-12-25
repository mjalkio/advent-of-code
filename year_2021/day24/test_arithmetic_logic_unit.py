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


@pytest.mark.parametrize(
    "valid_model_number",
    [
        ([9, 1, 5, 9, 9, 9, 9, 4, 3, 9, 9, 3, 9, 5]),
        ([7, 1, 1, 1, 1, 5, 9, 1, 1, 7, 6, 1, 5, 1]),
    ],
)
def test_manual_solutions(valid_model_number):
    assert run_program(read_puzzle_input(), valid_model_number)[z] == 0
