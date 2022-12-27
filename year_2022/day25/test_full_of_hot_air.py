import pytest

from util import read_puzzle_input
from year_2022.day25.full_of_hot_air import (
    decimal_to_snafu,
    snafu_to_decimal,
    sum_fuel_requirements,
)


SNAFU_DECIMAL_PAIRS = (
    ("1", 1),
    ("2", 2),
    ("1=", 3),
    ("1-", 4),
    ("10", 5),
    ("11", 6),
    ("12", 7),
    ("2=", 8),
    ("2-", 9),
    ("20", 10),
    ("1=0", 15),
    ("1-0", 20),
    ("1=11-2", 2022),
    ("1-0---0", 12345),
    ("1121-1110-1=0", 314159265),
    ("1=-0-2", 1747),
    ("12111", 906),
    ("2=0=", 198),
    ("21", 11),
    ("2=01", 201),
    ("111", 31),
    ("20012", 1257),
    ("112", 32),
    ("1=-1=", 353),
    ("1-12", 107),
    ("12", 7),
    ("1=", 3),
    ("122", 37),
)


def test_sum_fuel_requirements():
    assert sum_fuel_requirements(read_puzzle_input("test_input.txt")) == 4890


@pytest.mark.parametrize("snafu_num, decimal_num", SNAFU_DECIMAL_PAIRS)
def test_snafu_to_decimal(snafu_num, decimal_num):
    assert snafu_to_decimal(snafu_num) == decimal_num


@pytest.mark.parametrize("snafu_num, decimal_num", SNAFU_DECIMAL_PAIRS)
def test_decimal_to_snafu(snafu_num, decimal_num):
    assert decimal_to_snafu(decimal_num) == snafu_num
