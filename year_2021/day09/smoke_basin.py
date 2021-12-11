from math import prod

from util import read_puzzle_input


def get_low_point_risk_level_sum(puzzle_input):
    lines = puzzle_input.split("\n")
    risk_level = 0
    heightmap = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            heightmap[(x, y)] = int(lines[y][x])

    for (x, y), height in heightmap.items():
        adjacent = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        if all(
            heightmap[(xx, yy)] > height for xx, yy in adjacent if (xx, yy) in heightmap
        ):
            risk_level += height + 1

    return risk_level


def get_three_largest_basin_size_product(puzzle_input):
    lines = puzzle_input.split("\n")
    heightmap = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            heightmap[(x, y)] = int(lines[y][x])

    mapped_locations = set()
    basin_sizes = []
    for (x, y), height in heightmap.items():
        if height == 9 or (x, y) in mapped_locations:
            continue

        basin_sizes.append(0)
        to_visit = [(x, y)]
        while len(to_visit) > 0:
            xx, yy = to_visit.pop()
            if (xx, yy) in mapped_locations:
                continue

            mapped_locations.add((xx, yy))
            basin_sizes[-1] += 1
            to_visit += [
                coord
                for coord in [(xx - 1, yy), (xx, yy + 1), (xx + 1, yy), (xx, yy - 1)]
                if coord in heightmap
                and coord not in mapped_locations
                and heightmap[coord] != 9
            ]
    return prod(sorted(basin_sizes)[-3:])


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_low_point_risk_level_sum(puzzle_input)}")
    print(f"Part 2: {get_three_largest_basin_size_product(puzzle_input)}")
