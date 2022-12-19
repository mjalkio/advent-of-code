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
    max_x = 0
    max_y = 0
    max_z = 0
    for line in puzzle_input.strip().split("\n"):
        x, y, z = [int(num) for num in line.split(",")]
        cubes.add((x, y, z))
        max_x = max(x + 1, max_x)
        max_y = max(y + 1, max_y)
        max_z = max(z + 1, max_z)

    exterior_surface_area = 0
    # Start at 0, 0, 0 and let water flow out
    # Where we get stopped, we found an exterior surface
    stack = [(0, 0, 0)]
    explored = set(stack)
    while len(stack) > 0:
        x, y, z = stack.pop()
        for adjacent_cube in [
            (x + 1, y, z),
            (x - 1, y, z),
            (x, y + 1, z),
            (x, y - 1, z),
            (x, y, z + 1),
            (x, y, z - 1),
        ]:
            if x < 0 or y < 0 or z < 0 or x > max_x or y > max_y or z > max_z:
                continue
            elif adjacent_cube in cubes:
                exterior_surface_area += 1
            elif adjacent_cube not in explored:
                explored.add(adjacent_cube)
                stack.append(adjacent_cube)
    return exterior_surface_area


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {approximate_surface_area(puzzle_input)}")
    print(f"Part 2: {exterior_surface_area(puzzle_input)}")
