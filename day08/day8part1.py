import os.path as op


def get_input(filename):
    with open(op.join(op.dirname(__file__), filename), 'r') as f:
        puzzle_input = f.read()
    return puzzle_input


def get_largest_register_value(puzzle_input):
    return 0
