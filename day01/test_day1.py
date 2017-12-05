from .day1part1 import sum_matches
from .day1part2 import sum_matches2


def test_part1():
    test_cases = [
        ('1122', 3),
        ('1111', 4),
        ('1234', 0),
        ('91212129', 9),
    ]

    for puzzle_input, expected in test_cases:
        assert sum_matches(puzzle_input) == expected


def test_part2():
    test_cases = [
        ('1212', 6),
        ('1221', 0),
        ('123425', 4),
        ('123123', 12),
        ('12131415', 4),
    ]

    for puzzle_input, expected in test_cases:
        assert sum_matches2(puzzle_input) == expected
