from .day1part1 import sum_matches


def test_part1():
    test_cases = [
        ('1122', 3),
        ('1111', 4),
        ('1234', 0),
        ('91212129', 9),
    ]

    for puzzle_input, expected in test_cases:
        assert sum_matches(puzzle_input) == expected
