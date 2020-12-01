from .day3part1 import data_coordinates, spiral_manhattan_distance
from .day3part2 import first_spiral_value_larger


def test_data_coordinates():
    test_cases = [
        (1, (0, 0)),
        (2, (1, 0)),
        (12, (2, 1)),
        (13, (2, 2)),
        (22, (-1, -2)),
        (23, (0, -2)),
        (26, (3, -2)),
        (35, (-1, 3)),
    ]

    for data_loc, expected in test_cases:
        assert data_coordinates(data_loc) == expected


def test_part1():
    test_cases = [
        (1, 0),
        (12, 3),
        (23, 2),
        (1024, 31),
    ]

    for puzzle_input, expected in test_cases:
        assert spiral_manhattan_distance(puzzle_input) == expected


def test_part2():
    test_cases = [
        (1, 2),
        (4, 5),
        (5, 10),
        (8, 10),
        (100, 122),
        (300, 304),
        (-1, 1),
    ]

    for puzzle_input, expected in test_cases:
        assert first_spiral_value_larger(puzzle_input) == expected
