import pytest

from year_2020.day02.password_philosophy import is_valid_password, num_valid_passwords


@pytest.mark.parametrize(
    'character,min_usages,max_usages,password,expected',
    [
        ('a', 1, 3, 'abcde', True),
        ('b', 1, 2, 'cdefg', False),
        ('c', 2, 9, 'ccccccccc', True),
    ]
)
def test_is_valid_password(character, min_usages, max_usages, password, expected):
    assert is_valid_password(character, min_usages, max_usages, password) == expected


def test_num_valid_passwords():
    puzzle_input = """
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""
    assert num_valid_passwords(puzzle_input) == 2
