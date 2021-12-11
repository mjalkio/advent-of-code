from itertools import product

from util import read_puzzle_input

FLASHPOINT = 10


def get_num_flashes(puzzle_input, num_days=100):
    lines = puzzle_input.split("\n")
    energy_levels = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            energy_levels[(x, y)] = int(lines[y][x])

    num_flashes = 0
    for i in range(num_days):
        flashes = []
        for x, y in energy_levels.keys():
            energy_levels[(x, y)] += 1
            if energy_levels[(x, y)] == FLASHPOINT:
                flashes.append((x, y))

        while len(flashes) > 0:
            x, y = flashes.pop()
            num_flashes += 1
            for dx, dy in product(range(-1, 2), range(-1, 2)):
                coord = (x + dx, y + dy)
                if coord not in energy_levels:
                    continue

                energy_levels[coord] += 1
                if energy_levels[coord] == FLASHPOINT:
                    flashes.append(coord)

        for x, y in energy_levels.keys():
            if energy_levels[(x, y)] >= FLASHPOINT:
                energy_levels[(x, y)] = 0
    return num_flashes


def get_first_step_all_flash(puzzle_input):
    return 0


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_num_flashes(puzzle_input)}")
    print(f"Part 2: {get_first_step_all_flash(puzzle_input)}")
