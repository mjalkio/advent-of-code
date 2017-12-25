from itertools import chain


def flatten(list_of_lists):
    return list(chain.from_iterable(list_of_lists))


def get_root(puzzle_input):
    lines = puzzle_input.strip().split('\n')
    programs = [line[0:4] for line in lines]
    child_programs = flatten([line.split('->')[1].strip().split(', ')
                              for line in lines
                              if '->' in line])
    root = tuple(set(programs) - set(child_programs))
    assert len(root) == 1, 'Should only have a single root'
    return root[0]
