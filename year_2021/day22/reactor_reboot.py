from collections import namedtuple

from util import read_puzzle_input


Cuboid = namedtuple("Cuboid", ["min_x", "max_x", "min_y", "max_y", "min_z", "max_z"])


def _has_overlap(cuboid_a, cuboid_b):
    if (
        cuboid_a.min_x > cuboid_b.max_x
        or cuboid_b.min_x > cuboid_a.max_x
        or cuboid_a.min_y > cuboid_b.max_y
        or cuboid_b.min_y > cuboid_a.max_y
        or cuboid_a.min_z > cuboid_b.max_z
        or cuboid_b.min_z > cuboid_a.max_z
    ):
        return False

    return True


def _handle_overlap(cuboid_a, cuboid_b):
    # Return overlap, unique to a, unique to b
    overlap_min_x = max(cuboid_a.min_x, cuboid_b.min_x)
    overlap_max_x = min(cuboid_a.max_x, cuboid_b.max_x)

    overlap_min_y = max(cuboid_a.min_y, cuboid_b.min_y)
    overlap_max_y = min(cuboid_a.max_y, cuboid_b.max_y)

    overlap_min_z = max(cuboid_a.min_z, cuboid_b.min_z)
    overlap_max_z = min(cuboid_a.max_z, cuboid_b.max_z)

    overlap_cuboid = Cuboid(
        min_x=overlap_min_x,
        max_x=overlap_max_x,
        min_y=overlap_min_y,
        max_y=overlap_max_y,
        min_z=overlap_min_z,
        max_z=overlap_max_z,
    )

    a_subcuboids = []
    b_subcuboids = []

    if cuboid_a.min_x < overlap_min_x:
        a_subcuboids.append(
            Cuboid(
                min_x=cuboid_a.min_x,
                max_x=overlap_min_x - 1,
                min_y=cuboid_a.min_y,
                max_y=cuboid_a.max_y,
                min_z=cuboid_a.min_z,
                max_z=cuboid_a.max_z,
            )
        )
    if cuboid_b.min_x < overlap_min_x:
        b_subcuboids.append(
            Cuboid(
                min_x=cuboid_b.min_x,
                max_x=overlap_min_x - 1,
                min_y=cuboid_b.min_y,
                max_y=cuboid_b.max_y,
                min_z=cuboid_b.min_z,
                max_z=cuboid_b.max_z,
            )
        )

    if cuboid_a.min_y < overlap_min_y:
        a_subcuboids.append(
            Cuboid(
                min_x=overlap_min_x,
                max_x=overlap_max_x,
                min_y=cuboid_a.min_y,
                max_y=overlap_min_y - 1,
                min_z=cuboid_a.min_z,
                max_z=cuboid_a.max_z,
            )
        )
    if cuboid_b.min_y < overlap_min_y:
        b_subcuboids.append(
            Cuboid(
                min_x=overlap_min_x,
                max_x=overlap_max_x,
                min_y=cuboid_b.min_y,
                max_y=overlap_min_y - 1,
                min_z=cuboid_b.min_z,
                max_z=cuboid_b.max_z,
            )
        )

    if cuboid_a.min_z < overlap_min_z:
        a_subcuboids.append(
            Cuboid(
                min_x=overlap_min_x,
                max_x=overlap_max_x,
                min_y=overlap_min_y,
                max_y=overlap_max_y,
                min_z=cuboid_a.min_z,
                max_z=overlap_min_z - 1,
            )
        )
    if cuboid_b.min_z < overlap_min_z:
        b_subcuboids.append(
            Cuboid(
                min_x=overlap_min_x,
                max_x=overlap_max_x,
                min_y=overlap_min_y,
                max_y=overlap_max_y,
                min_z=cuboid_b.min_z,
                max_z=overlap_min_z - 1,
            )
        )

    if cuboid_a.max_x > overlap_max_x:
        a_subcuboids.append(
            Cuboid(
                min_x=overlap_max_x + 1,
                max_x=cuboid_a.max_x,
                min_y=cuboid_a.min_y,
                max_y=cuboid_a.max_y,
                min_z=cuboid_a.min_z,
                max_z=cuboid_a.max_z,
            )
        )
    if cuboid_b.max_x > overlap_max_x:
        b_subcuboids.append(
            Cuboid(
                min_x=overlap_max_x + 1,
                max_x=cuboid_b.max_x,
                min_y=cuboid_b.min_y,
                max_y=cuboid_b.max_y,
                min_z=cuboid_b.min_z,
                max_z=cuboid_b.max_z,
            )
        )

    if cuboid_a.max_y > overlap_max_y:
        a_subcuboids.append(
            Cuboid(
                min_x=overlap_min_x,
                max_x=overlap_max_x,
                min_y=overlap_max_y + 1,
                max_y=cuboid_a.max_y,
                min_z=cuboid_a.min_z,
                max_z=cuboid_a.max_z,
            )
        )
    if cuboid_b.max_y > overlap_max_y:
        b_subcuboids.append(
            Cuboid(
                min_x=overlap_min_x,
                max_x=overlap_max_x,
                min_y=overlap_max_y + 1,
                max_y=cuboid_b.max_y,
                min_z=cuboid_b.min_z,
                max_z=cuboid_b.max_z,
            )
        )

    if cuboid_a.max_z > overlap_max_z:
        a_subcuboids.append(
            Cuboid(
                min_x=overlap_min_x,
                max_x=overlap_max_x,
                min_y=overlap_min_y,
                max_y=overlap_max_y,
                min_z=overlap_max_z + 1,
                max_z=cuboid_a.max_z,
            )
        )
    if cuboid_b.max_z > overlap_max_z:
        b_subcuboids.append(
            Cuboid(
                min_x=overlap_min_x,
                max_x=overlap_max_x,
                min_y=overlap_min_y,
                max_y=overlap_max_y,
                min_z=overlap_max_z + 1,
                max_z=cuboid_b.max_z,
            )
        )

    return overlap_cuboid, a_subcuboids, b_subcuboids


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
            found_overlap = False

            for cuboid in on_cuboids:
                if not _has_overlap(next_cuboid, cuboid):
                    continue

                found_overlap = True

                on_cuboids.remove(cuboid)
                overlap, next_subcuboids, subcuboids = _handle_overlap(
                    next_cuboid, cuboid
                )
                if state == "on":
                    on_cuboids.add(overlap)
                    on_cuboids.update(subcuboids)
                else:
                    on_cuboids.update(subcuboids)

                cuboids_to_handle.update(next_subcuboids)
                break

            # Did not find an overlap
            if not found_overlap and state == "on":
                on_cuboids.add(next_cuboid)

    return sum(_get_area(cuboid) for cuboid in on_cuboids)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_num_cubes_on(puzzle_input)}")
    print(
        f"Part 2: {get_num_cubes_on(puzzle_input, is_initialization_procedure=False)}"
    )
