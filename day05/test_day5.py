from day5part1 import num_jumps
from day5part2 import num_jumps_again

INSTRUCTIONS = [0, 3, 0, 1, -3]


def test_num_jumps():
    assert num_jumps(INSTRUCTIONS) == 5


def test_num_jumps_again():
    assert num_jumps_again(INSTRUCTIONS) == 10
