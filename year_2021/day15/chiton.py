import heapq
from collections import namedtuple

from util import read_puzzle_input

Node = namedtuple("Node", ["estimated_risk", "lowest_risk_to", "x", "y"])

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
                        added_risk = dx + dy
                        risk = risk_map[x, y] + added_risk
                        while risk > MAX_POSITION_RISK:
                            risk -= MAX_POSITION_RISK
                        risk_map[position] = risk

    max_x = max(x for x, y in risk_map.keys())
    max_y = max(y for x, y in risk_map.keys())
    # A*, A-star, A star, Dijkstra's (tagging this for searching in later years)
    to_visit = [Node(estimated_risk=max_x + max_y, lowest_risk_to=0, x=0, y=0)]
    lowest_risk_to = {coord: MAX_TOTAL_RISK for coord in risk_map.keys()}
    lowest_risk_to[(0, 0)] = 0

    while len(to_visit) > 0:
        current_node = heapq.heappop(to_visit)
        if current_node.x == max_x and current_node.y == max_y:
            # This is the goal node
            return current_node.lowest_risk_to

        x = current_node.x
        y = current_node.y
        neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for (x, y) in neighbors:
            if (x, y) not in risk_map:
                continue
            risk_to = current_node.lowest_risk_to + risk_map[(x, y)]
            if risk_to < lowest_risk_to[(x, y)]:
                lowest_risk_to[(x, y)] = risk_to
                heuristic_distance = max_x - x + max_y - y
                heapq.heappush(
                    to_visit,
                    Node(
                        estimated_risk=risk_to + heuristic_distance,
                        lowest_risk_to=risk_to,
                        x=x,
                        y=y,
                    ),
                )


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_lowest_risk_path_risk(puzzle_input)}")
    print(f"Part 2: {get_lowest_risk_path_risk(puzzle_input, use_full_map=True)}")
