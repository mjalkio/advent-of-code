import pytest

from year_2019.day04.secure_container import (
    is_valid,
)


@pytest.mark.parametrize(
    "password,expected_output",
    [
        ("111111", True),
        ("223450", False),
        ("123789", False),
        ("111123", True),
        ("122345", True),
    ],
)
def test_is_valid(password, expected_output):
    assert is_valid(password) == expected_output
