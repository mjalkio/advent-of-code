from util import read_puzzle_input


def approximate_surface_area(puzzle_input):
    cubes = set()
    for line in puzzle_input.strip().split("\n"):
        x, y, z = [int(num) for num in line.split(",")]
        cubes.add((x, y, z))

    approx_surface_area = 0
    for x, y, z in cubes:
        for adjacent_cube in [
            (x + 1, y, z),
            (x - 1, y, z),
            (x, y + 1, z),
            (x, y - 1, z),
            (x, y, z + 1),
            (x, y, z - 1),
        ]:
            if adjacent_cube not in cubes:
                approx_surface_area += 1
    return approx_surface_area


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {approximate_surface_area(puzzle_input)}")
    print(f"Part 2: {approximate_surface_area(puzzle_input)}")
