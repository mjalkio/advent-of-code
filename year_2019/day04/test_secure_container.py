import pytest

from year_2019.day04.secure_container import (
    is_valid,
)


@pytest.mark.parametrize(
    "password,strict,expected_output",
    [
        ("111111", False, True),
        ("223450", False, False),
        ("123789", False, False),
        ("111123", False, True),
        ("122345", False, True),
        ("112233", True, True),
        ("123444", True, False),
        ("111122", True, True),
    ],
)
def test_is_valid(password, expected_output, strict):
    assert is_valid(password, strict=strict) == expected_output
