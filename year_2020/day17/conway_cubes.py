from collections import UserDict

from util import read_puzzle_input

ACTIVE = '#'
INACTIVE = '.'


class EnergySource(UserDict):
    def __repr__(self):
        output = []
        z_coordinates = list(self.keys())
        z_coordinates.sort()
        for z in z_coordinates:
            output.append(f"z={z}")
            layer = self[z]
            width = max(x for x, y in layer.keys()) + 1
            height = max(y for x, y in layer.keys()) + 1
            for y in range(height):
                line = []
                for x in range(width):
                    line.append(layer[(x, y)])
                output.append(''.join(line))
            output.append('\n')

        return '\n'.join(output)


def _get_energy_source(puzzle_input):
    lines = [line for line in puzzle_input.split('\n') if line != '']
    initial_slice = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            initial_slice[(x, y)] = lines[y][x]
    return EnergySource({0: initial_slice})


def get_num_active_cubes(puzzle_input, num_cycles=6):
    energy_source = _get_energy_source(puzzle_input)
    return None


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_num_active_cubes(puzzle_input)}")
    print(f"Part 2: {None}")
