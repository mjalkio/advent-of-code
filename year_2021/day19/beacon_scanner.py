from collections import deque, namedtuple

from util import read_puzzle_input

NUM_ORIENTATIONS = 24
SHARED_BEACON_REQUIREMENT = 12
Point = namedtuple("Point", ["x", "y", "z"])


def _get_all_orientations(beacons):
    all_orientations = []
    for _ in range(NUM_ORIENTATIONS):
        all_orientations.append([])

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


def _orient_scanner(unoriented_scanner, oriented_scanners):
    for o_scanner in oriented_scanners:
        for o_ref_point in o_scanner:
            oriented_distances = set()
            for o_point in o_scanner:
                oriented_distances.add(
                    Point(
                        x=o_ref_point.x - o_point.x,
                        y=o_ref_point.y - o_point.y,
                        z=o_ref_point.z - o_point.z,
                    )
                )
            for orientation in _get_all_orientations(unoriented_scanner):
                for ref_point in orientation:
                    distances = set()
                    for point in orientation:
                        distances.add(
                            Point(
                                x=ref_point.x - point.x,
                                y=ref_point.y - point.y,
                                z=ref_point.z - point.z,
                            )
                        )

                    if len(distances.intersection(oriented_distances)) >= 12:
                        x_diff = o_ref_point.x - ref_point.x
                        y_diff = o_ref_point.y - ref_point.y
                        z_diff = o_ref_point.z - ref_point.z
                        newly_oriented_scanner = [
                            Point(
                                x=p.x + x_diff,
                                y=p.y + y_diff,
                                z=p.z + z_diff,
                            )
                            for p in unoriented_scanner
                        ]
                        return newly_oriented_scanner
    return None


def get_num_beacons(puzzle_input):
    lines = puzzle_input.split("\n")
    scanners = deque()
    for line in lines:
        if line == "":
            continue
        if "scanner" in line:
            scanners.append([])
        else:
            x, y, z = [int(val) for val in line.split(",")]
            scanners[-1].append(Point(x=x, y=y, z=z))

    oriented_scanners = [scanners.popleft()]

    while len(scanners) > 0:
        unoriented_scanner = scanners.popleft()
        newly_oriented_scanner = _orient_scanner(
            unoriented_scanner=unoriented_scanner, oriented_scanners=oriented_scanners
        )
        if newly_oriented_scanner is None:
            scanners.append(unoriented_scanner)
        else:
            oriented_scanners.append(newly_oriented_scanner)

    return len(set().union(*oriented_scanners))


if __name__ == "__main__":
    puzzle_input = read_puzzle_input("test_input.txt")

    print(f"Part 1: {get_num_beacons(puzzle_input)}")
    print(f"Part 2: {get_num_beacons(puzzle_input)}")
