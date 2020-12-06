import pytest

from year_2020.day05.binary_boarding import (
    seat_column,
    seat_id,
    seat_row,
)

TEST_CASES = [
    {
        'space_partitioning': 'FBFBBFFRLR',
        'row': 44,
        'column': 5,
        'id': 357,
    },
    {
        'space_partitioning': 'BFFFBBFRRR',
        'row': 70,
        'column': 7,
        'id': 567,
    },
    {
        'space_partitioning': 'FFFBBBFRRR',
        'row': 14,
        'column': 7,
        'id': 119,
    },
    {
        'space_partitioning': 'FBFBBFFRLR',
        'row': 102,
        'column': 4,
        'id': 820,
    },
]


@pytest.mark.parametrize(
    'column_space_partitioning,expected',
    [(case['space_partitioning'][:7], case['row']) for case in TEST_CASES]
)
def test_seat_column(column_space_partitioning, expected):
    assert seat_column(column_space_partitioning=column_space_partitioning) == expected


@pytest.mark.parametrize(
    'space_partitioning,expected',
    [(case['space_partitioning'], case['id']) for case in TEST_CASES]
)
def test_seat_id(space_partitioning, expected):
    assert seat_id(space_partitioning=space_partitioning) == expected


@pytest.mark.parametrize(
    'row_space_partitioning,expected',
    [(case['space_partitioning'][7:], case['id']) for case in TEST_CASES]
)
def test_seat_row(row_space_partitioning, expected):
    assert seat_row(row_space_partitioning=row_space_partitioning) == expected
