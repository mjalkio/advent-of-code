from .day2part1 import calculate_checksum


def test_part1():
    puzzle_input = """
        5 1 9 5
        7 5 3
        2 4 6 8
    """

    assert calculate_checksum(puzzle_input) == 18
