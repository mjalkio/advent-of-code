from .day3part1 import data_coordinates, spiral_manhattan_distance


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
