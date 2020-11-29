from .day2part1 import calculate_checksum
from .day2part2 import calculate_checksum_divisible


def test_part1():
    puzzle_input = """
        5 1 9 5
        7 5 3
        2 4 6 8
    """

    assert calculate_checksum(puzzle_input) == 18


def test_part2():
    puzzle_input = """
        5 9 2 8
        9 4 7 3
        3 8 6 5
    """

    assert calculate_checksum_divisible(puzzle_input) == 9
