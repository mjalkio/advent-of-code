from collections import namedtuple

from util import read_puzzle_input

NUM_ORIENTATIONS = 24
Point = namedtuple("Point", ["x", "y", "z"])


def _get_all_orientations(beacons):
    all_orientations = [[]] * NUM_ORIENTATIONS
    for x, y, z in beacons:
        all_point_orientations = [
            Point(x=x, y=y, z=z),
            Point(x=x, y=-z, z=y),
            Point(x=x, y=-y, z=-z),
            Point(x=x, y=z, z=-y),
            Point(x=y, y=-x, z=z),
            Point(x=y, y=-z, z=-x),
            Point(x=y, y=x, z=-z),
            Point(x=y, y=z, z=x),
            Point(x=-x, y=-y, z=z),
            Point(x=-x, y=-z, z=-y),
            Point(x=-x, y=y, z=-z),
            Point(x=-x, y=z, z=y),
            Point(x=-y, y=x, z=z),
            Point(x=-y, y=-z, z=x),
            Point(x=-y, y=-x, z=-z),
            Point(x=-y, y=z, z=-x),
            Point(x=z, y=y, z=-x),
            Point(x=z, y=x, z=y),
            Point(x=z, y=-y, z=x),
            Point(x=z, y=-x, z=-y),
            Point(x=-z, y=y, z=x),
            Point(x=-z, y=-x, z=y),
            Point(x=-z, y=-y, z=-x),
            Point(x=-z, y=x, z=-y),
        ]
        for i in range(NUM_ORIENTATIONS):
            all_orientations[i].append(all_point_orientations[i])

    return all_orientations


def get_num_beacons(puzzle_input):
    lines = puzzle_input.split("\n")
    scanner_beacons = []
    for line in lines:
        if line == "":
            continue
        if "scanner" in line:
            scanner_beacons.append([])
        else:
            x, y, z = [int(val) for val in line.split(",")]
            scanner_beacons[-1].append(Point(x=x, y=y, z=z))

    return 0


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_num_beacons(puzzle_input)}")
    print(f"Part 2: {get_num_beacons(puzzle_input)}")
