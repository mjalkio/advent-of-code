import pytest

from year_2020.day02.password_philosophy import (
    is_valid_password_part_1,
    num_valid_passwords_part_1,
    is_valid_password_part_2,
    num_valid_passwords_part_2,
)


@pytest.mark.parametrize(
    'character,min_usages,max_usages,password,expected',
    [
        ('a', 1, 3, 'abcde', True),
        ('b', 1, 2, 'cdefg', False),
        ('c', 2, 9, 'ccccccccc', True),
    ]
)
def test_is_valid_password_part_1(character, min_usages, max_usages, password, expected):
    assert is_valid_password_part_1(character, min_usages, max_usages, password) == expected


def test_num_valid_passwords_part_1():
    puzzle_input = """
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""
    assert num_valid_passwords_part_1(puzzle_input) == 2


@pytest.mark.parametrize(
    'character,position_1,position_2,password,expected',
    [
        ('a', 1, 3, 'abcde', True),
        ('b', 1, 2, 'cdefg', False),
        ('c', 2, 9, 'ccccccccc', False),
    ]
)
def test_is_valid_password_part_2(character, position_1, position_2, password, expected):
    assert is_valid_password_part_2(character, position_1, position_2, password) == expected


def test_num_valid_passwords_part_2():
    puzzle_input = """
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""
    assert num_valid_passwords_part_2(puzzle_input) == 1
