from util import read_puzzle_input

DIRECTION_MAP = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1),
}


def _is_touching(x1, y1, x2, y2):
    return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1


def num_positions_tail_visits(puzzle_input, num_knots=2):
    steps = []
    for line in puzzle_input.split("\n"):
        if line == "":
            continue
        direction, num_steps = line.split()
        steps += [DIRECTION_MAP[direction]] * int(num_steps)

    knot_positions = [(0, 0)] * num_knots
    tail_positions = set()
    tail_positions.add(knot_positions[-1])
    for dx, dy in steps:
        knot_positions[0] = (knot_positions[0][0] + dx, knot_positions[0][1] + dy)

        for i in range(1, num_knots):
            knot_1_x = knot_positions[i - 1][0]
            knot_1_y = knot_positions[i - 1][1]
            knot_2_x = knot_positions[i][0]
            knot_2_y = knot_positions[i][1]

            if _is_touching(knot_1_x, knot_1_y, knot_2_x, knot_2_y):
                continue

            if knot_1_x > knot_2_x:
                knot_2_x += 1
            elif knot_1_x < knot_2_x:
                knot_2_x -= 1

            if knot_1_y > knot_2_y:
                knot_2_y += 1
            elif knot_1_y < knot_2_y:
                knot_2_y -= 1

            knot_positions[i] = (knot_2_x, knot_2_y)

        tail_positions.add(knot_positions[-1])
    return len(tail_positions)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {num_positions_tail_visits(puzzle_input)}")
    print(f"Part 2: {num_positions_tail_visits(puzzle_input, num_knots=10)}")
