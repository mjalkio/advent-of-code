import os.path as op

from day7part1 import get_root


def get_input(filename):
    with open(op.join(op.dirname(__file__), filename), 'r') as f:
        puzzle_input = f.read()
    return puzzle_input


def test_get_root():
    puzzle_input = get_input('example.txt')
    assert get_root(puzzle_input) == 'tknk'
