from .day3part1 import spiral_manhattan_distance


def test_part1():
    test_cases = [
        ('1', 0),
        ('12', 3),
        ('23', 2),
        ('1024', 31),
    ]

    for puzzle_input, expected in test_cases:
        assert spiral_manhattan_distance(puzzle_input) == expected
