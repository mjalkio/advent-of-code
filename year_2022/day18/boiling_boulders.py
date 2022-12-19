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


def exterior_surface_area(puzzle_input):
    cubes = set()
    x_limits = {}
    y_limits = {}
    z_limits = {}
    for line in puzzle_input.strip().split("\n"):
        x, y, z = [int(num) for num in line.split(",")]
        cubes.add((x, y, z))

        if (y, z) not in x_limits:
            x_limits[y, z] = (x, x)
        else:
            x_min, x_max = x_limits[y, z]
            x_limits[y, z] = (min(x_min, x), max(x_max, x))

        if (x, z) not in y_limits:
            y_limits[x, z] = (y, y)
        else:
            y_min, y_max = y_limits[x, z]
            y_limits[x, z] = (min(y_min, y), max(y_max, y))

        if (x, y) not in z_limits:
            z_limits[x, y] = (z, z)
        else:
            z_min, z_max = z_limits[x, y]
            z_limits[x, y] = (min(z_min, z), max(z_max, z))

    surface_area = 0
    for x, y, z in cubes:
        x_min, x_max = x_limits[y, z]
        y_min, y_max = y_limits[x, z]
        z_min, z_max = z_limits[x, y]

        comparisons = [
            (x, x_min),
            (x, x_max),
            (y, y_min),
            (y, y_max),
            (z, z_min),
            (z, z_max),
        ]
        surface_area += sum(coord == limit for coord, limit in comparisons)
    return surface_area


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {approximate_surface_area(puzzle_input)}")
    print(f"Part 2: {exterior_surface_area(puzzle_input)}")
