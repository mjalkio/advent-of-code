from util import read_puzzle_input

ACTIVE = '#'
INACTIVE = '.'


def _get_energy_source(puzzle_input):
    lines = [line for line in puzzle_input.split('\n') if line != '']
    initial_slice = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            initial_slice[(x, y)] = lines[y][x]
    return {0: initial_slice}


def get_num_active_cubes(puzzle_input, num_cycles=6):
    energy_source = _get_energy_source(puzzle_input)
    return None


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_num_active_cubes(puzzle_input)}")
    print(f"Part 2: {None}")
