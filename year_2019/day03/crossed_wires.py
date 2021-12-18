from util import read_puzzle_input


def _get_wire_points(wire):
    points = set()
    num_steps_to_point = {}
    location = [0, 0]
    num_steps = 0
    for segment in wire.split(","):
        orientation = segment[0]
        length = int(segment[1:])
        if orientation == "R":
            axis = 0
            direction = 1
        if orientation == "L":
            axis = 0
            direction = -1
        if orientation == "U":
            axis = 1
            direction = 1
        if orientation == "D":
            axis = 1
            direction = -1
        for _ in range(length):
            location[axis] += direction
            num_steps += 1
            point = tuple(location)
            points.add(point)
            if point not in num_steps_to_point:
                num_steps_to_point[point] = num_steps

    return points, num_steps_to_point


def _manhattan_distance(point_a, point_b=(0, 0)):
    return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])


def get_distance_closest_intersection(puzzle_input):
    wire_1, wire_2 = puzzle_input.split("\n")
    wire_1_points, _ = _get_wire_points(wire_1)
    wire_2_points, _ = _get_wire_points(wire_2)
    intersections = wire_1_points.intersection(wire_2_points)
    return min(_manhattan_distance(point) for point in intersections)


def get_fewest_combined_steps(puzzle_input):
    wire_1, wire_2 = puzzle_input.split("\n")
    wire_1_points, wire_1_steps_to_point = _get_wire_points(wire_1)
    wire_2_points, wire_2_steps_to_point = _get_wire_points(wire_2)
    intersections = wire_1_points.intersection(wire_2_points)
    return min(
        wire_1_steps_to_point[point] + wire_2_steps_to_point[point]
        for point in intersections
    )


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_distance_closest_intersection(puzzle_input)}")
    print(f"Part 2: {get_fewest_combined_steps(puzzle_input)}")
