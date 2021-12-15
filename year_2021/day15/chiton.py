from collections import namedtuple

from util import read_puzzle_input

Path = namedtuple("Path", ["positions", "risk"])

MAX_POSITION_RISK = 9
# Arbitrary large number
MAX_TOTAL_RISK = 1_000_000_000
NUM_TIMES_LARGER = 5


def _print_map(risk_map):
    width = max(x for x, _ in risk_map) + 1
    height = max(y for _, y in risk_map) + 1
    for y in range(height):
        line = []
        for x in range(width):
            line.append(str(risk_map[(x, y)]))
        print("".join(line))


def get_lowest_risk_path_risk(puzzle_input, use_full_map=False):
    lines = puzzle_input.split("\n")
    risk_map = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            risk_map[(x, y)] = int(lines[y][x])

    if use_full_map:
        width = x + 1
        height = y + 1
        for x in range(width):
            for y in range(height):
                for dx in range(0, NUM_TIMES_LARGER):
                    for dy in range(0, NUM_TIMES_LARGER):
                        if (dx, dy) == (0, 0):
                            continue

                        position = (x + dx * width, y + dy * height)
                        added_risk = dx + 1 if dx == dy else max(dx, dy)
                        risk = (risk_map[x, y] + added_risk) % (MAX_POSITION_RISK + 1)
                        risk_map[position] = risk

    _print_map(risk_map)
    width = max(x for x, y in risk_map.keys()) + 1
    height = max(y for x, y in risk_map.keys()) + 1
    risk_to_destination = {}
    for x in reversed(range(width)):
        for y in reversed(range(height)):
            if len(risk_to_destination) == 0:
                risk_to_destination[(x, y)] = risk_map[(x, y)]
                continue

            risk_to_destination[(x, y)] = (
                min(
                    risk_to_destination.get((x + 1, y), MAX_TOTAL_RISK),
                    risk_to_destination.get((x, y + 1), MAX_TOTAL_RISK),
                )
                + risk_map[(x, y)]
            )
    return risk_to_destination[(0, 0)] - risk_map[(0, 0)]


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_lowest_risk_path_risk(puzzle_input)}")
    print(f"Part 2: {get_lowest_risk_path_risk(puzzle_input, use_full_map=True)}")
