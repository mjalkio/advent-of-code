import pytest

from year_2020.day15.rambunctious_recitation import get_number_spoken


@pytest.mark.parametrize(
    'starting_numbers,num_turns,expected',
    [
        ('0,3,6', 1, 0),
        ('0,3,6', 2, 3),
        ('0,3,6', 3, 6),
        ('0,3,6', 4, 0),
        ('0,3,6', 5, 3),
        ('0,3,6', 6, 3),
        ('0,3,6', 7, 1),
        ('0,3,6', 8, 0),
        ('0,3,6', 9, 4),
        ('0,3,6', 10, 0),
        ('0,3,6', 2020, 436),
        ('1,3,2', 2020, 1),
        ('2,1,3', 2020, 10),
        ('1,2,3', 2020, 27),
        ('2,3,1', 2020, 78),
        ('3,2,1', 2020, 438),
        ('3,1,2', 2020, 1836),
    ]
)
def test_get_number_spoken(starting_numbers, num_turns, expected):
    assert get_number_spoken(starting_numbers, num_turns) == expected
