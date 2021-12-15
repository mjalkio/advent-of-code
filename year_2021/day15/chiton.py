from collections import namedtuple

from util import read_puzzle_input

Path = namedtuple("Path", ["positions", "risk"])

# Arbitrary large number
MAX_RISK = 1_000_000_000


def get_lowest_risk_path_risk(puzzle_input, use_full_map=False):
    lines = puzzle_input.split("\n")
    risk_map = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            risk_map[(x, y)] = int(lines[y][x])

    risk_to_destination = {}
    for x in reversed(range(len(lines[0]))):
        for y in reversed(range(len(lines))):
            if len(risk_to_destination) == 0:
                risk_to_destination[(x, y)] = risk_map[(x, y)]
                continue

            risk_to_destination[(x, y)] = (
                min(
                    risk_to_destination.get((x + 1, y), MAX_RISK),
                    risk_to_destination.get((x, y + 1), MAX_RISK),
                )
                + risk_map[(x, y)]
            )
    return risk_to_destination[(0, 0)] - risk_map[(0, 0)]


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_lowest_risk_path_risk(puzzle_input)}")
    print(f"Part 2: {get_lowest_risk_path_risk(puzzle_input, use_full_map=True)}")
