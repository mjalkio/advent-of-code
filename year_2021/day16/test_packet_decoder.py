import pytest

from util import read_puzzle_input
from year_2021.day16.packet_decoder import (
    get_version_sum_from_input,
    get_version_sum_from_packet,
    hex_to_bin,
)


@pytest.mark.parametrize(
    "hex_input,binary_output",
    [
        ("D2FE28", "110100101111111000101000"),
        ("38006F45291200", "00111000000000000110111101000101001010010001001000000000"),
        ("EE00D40C823060", "11101110000000001101010000001100100000100011000001100000"),
    ],
)
def test_hex_to_bin(hex_input, binary_output):
    assert hex_to_bin(hex_input) == binary_output


@pytest.mark.parametrize(
    "binary_input,expected",
    [
        ("11101110000000001101010000001100100000100011000001100000", 7 + 2 + 4 + 1),
        ("00111000000000000110111101000101001010010001001000000000", 1 + 6 + 2),
    ],
)
def test_subpackets(binary_input, expected):
    assert (
        get_version_sum_from_packet(
            binary_input
        )[0]
        == expected
    )


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("test_input1.txt", 16),
        ("test_input2.txt", 12),
        ("test_input3.txt", 23),
        ("test_input4.txt", 31),
    ],
)
def test_get_version_sum_from_input(test_input, expected):
    assert get_version_sum_from_input(read_puzzle_input(test_input)) == expected
