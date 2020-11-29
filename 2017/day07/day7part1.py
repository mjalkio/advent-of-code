import os.path as op
from itertools import chain


def get_input(filename):
    with open(op.join(op.dirname(__file__), filename), 'r') as f:
        puzzle_input = f.read()
    return puzzle_input


def flatten(list_of_lists):
    return list(chain.from_iterable(list_of_lists))


def get_root(puzzle_input):
    lines = puzzle_input.strip().split('\n')
    programs = [line.split('(')[0].strip() for line in lines]
    child_programs = flatten([line.split('->')[1].strip().split(', ')
                              for line in lines
                              if '->' in line])
    root = tuple(set(programs) - set(child_programs))
    assert len(root) == 1, 'Should only have a single root'
    return root[0]


if __name__ == '__main__':
    puzzle_input = get_input('puzzle_input.txt')
    print(get_root(puzzle_input))
