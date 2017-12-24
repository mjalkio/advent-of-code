from day5part1 import num_jumps


def test_num_jumps():
    instructions = [0, 3, 0, 1, -3]
    assert num_jumps(instructions) == 5
