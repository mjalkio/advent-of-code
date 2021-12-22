from util import read_puzzle_input


def get_num_cubes_on(puzzle_input, is_initialization_procedure=True):
    on_cubes = set()
    for step in puzzle_input.split("\n"):
        state, cuboid = step.split(" ")
        x_range, y_range, z_range = [rng[2:].split("..") for rng in cuboid.split(",")]
        min_x, max_x = [int(num) for num in x_range]
        min_y, max_y = [int(num) for num in y_range]
        min_z, max_z = [int(num) for num in z_range]

        if is_initialization_procedure and any(
            abs(num) > 50 for num in [min_x, max_x, min_y, max_y, min_z, max_z]
        ):
            continue

        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                for z in range(min_z, max_z + 1):

                    if state == "on":
                        on_cubes.add((x, y, z))
                    else:
                        on_cubes.discard((x, y, z))

    return len(on_cubes)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_num_cubes_on(puzzle_input)}")
    print(
        f"Part 2: {get_num_cubes_on(puzzle_input, is_initialization_procedure=False)}"
    )
