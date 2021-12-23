from collections import namedtuple

from util import read_puzzle_input


Cuboid = namedtuple("Cuboid", ["min_x", "max_x", "min_y", "max_y", "min_z", "max_z"])


def _overlaps(cuboid_a, cuboid_b):
    return False


def _handle_overlap(cuboid_a, cuboid_b):
    # Return overlap, unique to a, unique to b
    return None, [cuboid_a], [cuboid_b]


def _get_area(cuboid):
    num_x = cuboid.max_x - cuboid.min_x + 1
    num_y = cuboid.max_y - cuboid.min_y + 1
    num_z = cuboid.max_z - cuboid.min_z + 1

    return num_x * num_y * num_z


def get_num_cubes_on(puzzle_input, is_initialization_procedure=True):
    on_cuboids = set()
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

        cuboids_to_handle = set(
            [
                Cuboid(
                    min_x=min_x,
                    max_x=max_x,
                    min_y=min_y,
                    max_y=max_y,
                    min_z=min_z,
                    max_z=max_z,
                )
            ]
        )

        while len(cuboids_to_handle) > 0:
            next_cuboid = cuboids_to_handle.pop()

            for cuboid in on_cuboids:
                if not _overlaps(next_cuboid, cuboid):
                    continue

                on_cuboids.remove(cuboid)
                overlap, next_subcuboids, subcuboids = _handle_overlap(
                    next_cuboid, cuboid
                )
                if state == "on":
                    on_cuboids.add(overlap)
                    on_cuboids.update(subcuboids)
                else:
                    cuboids_to_handle.update(subcuboids)

                cuboids_to_handle.update(next_subcuboids)
                break

            # Did not find an overlap
            if state == "on":
                on_cuboids.add(next_cuboid)

    return sum(_get_area(cuboid) for cuboid in on_cuboids)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_num_cubes_on(puzzle_input)}")
    print(
        f"Part 2: {get_num_cubes_on(puzzle_input, is_initialization_procedure=False)}"
    )
