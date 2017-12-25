from day7part1 import get_input, get_root
from day7part2 import wrong_weight_disc_correction


def test_get_root():
    puzzle_input = get_input('example.txt')
    assert get_root(puzzle_input) == 'tknk'


def test_wrong_weight_disc_correction():
    puzzle_input = get_input('example.txt')
    assert wrong_weight_disc_correction(puzzle_input) == 60
