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


def _get_num_active_neighbors(x, y, z, energy_source):
    num_active_neighbors = 0
    for neighbor_z in range(z - 1, z + 2):
        layer = energy_source.get(neighbor_z, {})

        for neighbor_x in range(x - 1, x + 2):
            for neighbor_y in range(y - 1, y + 2):
                if neighbor_x == x and neighbor_y == y and neighbor_z == z:
                    continue

                if layer.get((neighbor_x, neighbor_y), INACTIVE) == ACTIVE:
                    num_active_neighbors += 1
    return num_active_neighbors


def get_num_active_cubes(puzzle_input, num_cycles=6):
    energy_source = _get_energy_source(puzzle_input)
    for cycle in range(num_cycles):
        curr_max_z = max(energy_source.keys())
        curr_min_z = min(energy_source.keys())
        curr_max_x = max(x for x, y in energy_source[0])
        curr_min_x = min(x for x, y in energy_source[0])
        curr_max_y = max(y for x, y in energy_source[0])
        curr_min_y = min(y for x, y in energy_source[0])

        next_state = {}
        for z in range(curr_min_z - 1, curr_max_z + 2):
            layer = {}
            for x in range(curr_min_x - 1, curr_max_x + 2):
                for y in range(curr_min_y - 1, curr_max_y + 2):
                    curr_cube_state = energy_source.get(z, {}).get((x, y), INACTIVE)
                    num_active_neighbors = _get_num_active_neighbors(x, y, z, energy_source)
                    if curr_cube_state == ACTIVE:
                        if num_active_neighbors in (2, 3):
                            layer[(x, y)] = ACTIVE
                        else:
                            layer[(x, y)] = INACTIVE
                    else:
                        if num_active_neighbors == 3:
                            layer[(x, y)] = ACTIVE
                        else:
                            layer[(x, y)] = INACTIVE
            next_state[z] = layer
        energy_source = EnergySource(next_state)

    num_active_cubes = 0
    for layer in energy_source.values():
        num_active_cubes += sum(cube == ACTIVE for cube in layer.values())
    return num_active_cubes


def _get_num_active_neighbors_4d(x, y, z, w, energy_source):
    num_active_neighbors = 0
    for neighbor_w in range(w - 1, w + 2):
        for neighbor_z in range(z - 1, z + 2):
            layer = energy_source.get(neighbor_w, {}).get(neighbor_z, {})

            for neighbor_x in range(x - 1, x + 2):
                for neighbor_y in range(y - 1, y + 2):
                    if neighbor_x == x and neighbor_y == y and neighbor_z == z and neighbor_w == w:
                        continue

                    if layer.get((neighbor_x, neighbor_y), INACTIVE) == ACTIVE:
                        num_active_neighbors += 1
    return num_active_neighbors


def get_num_active_cubes_4d(puzzle_input, num_cycles=6):  # noqa
    lines = [line for line in puzzle_input.split('\n') if line != '']
    initial_layer = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            initial_layer[(x, y)] = lines[y][x]

    energy_source = {0: {0: initial_layer}}
    for cycle in range(num_cycles):
        curr_max_w = max(energy_source.keys())
        curr_min_w = min(energy_source.keys())
        curr_max_z = max(energy_source[0].keys())
        curr_min_z = min(energy_source[0].keys())
        curr_max_x = max(x for x, y in energy_source[0][0])
        curr_min_x = min(x for x, y in energy_source[0][0])
        curr_max_y = max(y for x, y in energy_source[0][0])
        curr_min_y = min(y for x, y in energy_source[0][0])

        next_state = {}
        for w in range(curr_min_w - 1, curr_max_w + 2):
            next_w = {}
            for z in range(curr_min_z - 1, curr_max_z + 2):
                layer = {}
                for x in range(curr_min_x - 1, curr_max_x + 2):
                    for y in range(curr_min_y - 1, curr_max_y + 2):
                        curr_cube_state = energy_source.get(w, {}).get(z, {}).get((x, y), INACTIVE)
                        num_active_neighbors = _get_num_active_neighbors_4d(
                            x,
                            y,
                            z,
                            w,
                            energy_source
                        )
                        if curr_cube_state == ACTIVE:
                            if num_active_neighbors in (2, 3):
                                layer[(x, y)] = ACTIVE
                            else:
                                layer[(x, y)] = INACTIVE
                        else:
                            if num_active_neighbors == 3:
                                layer[(x, y)] = ACTIVE
                            else:
                                layer[(x, y)] = INACTIVE
                next_w[z] = layer
            next_state[w] = next_w
        energy_source = next_state

    num_active_cubes = 0
    for w in energy_source.keys():
        for layer in energy_source[w].values():
            num_active_cubes += sum(cube == ACTIVE for cube in layer.values())
    return num_active_cubes


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_num_active_cubes(puzzle_input)}")
    print(f"Part 2: {get_num_active_cubes_4d(puzzle_input)}")
