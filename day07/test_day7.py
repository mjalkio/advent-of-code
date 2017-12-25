from day7part1 import get_input, get_root


def test_get_root():
    puzzle_input = get_input('example.txt')
    assert get_root(puzzle_input) == 'tknk'
