from collections import namedtuple

from util import read_puzzle_input

Path = namedtuple("Path", ["positions", "risk"])


def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


def get_lowest_risk_path_risk(puzzle_input):
    lines = puzzle_input.split("\n")
    risk_map = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            risk_map[(x, y)] = int(lines[y][x])

    destination_position = (x, y)
    lowest_risk = 1_000_000_000  # Assuming the actual result will be lower than this
    potential_paths = [Path(positions=[(0, 0)], risk=0)]

    while len(potential_paths) > 0:
        path_to_consider = potential_paths.pop()
        if path_to_consider.risk >= lowest_risk:
            continue

        x, y = path_to_consider.positions[-1]
        if (x, y) == destination_position:
            if path_to_consider.risk < lowest_risk:
                lowest_risk = path_to_consider.risk
            continue

        for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if (i, j) in risk_map and (i, j) not in path_to_consider.positions:
                potential_paths.append(
                    Path(
                        positions=path_to_consider.positions.copy() + [(i, j)],
                        risk=path_to_consider.risk + risk_map[(i, j)],
                    )
                )
    return lowest_risk


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_lowest_risk_path_risk(puzzle_input)}")
    print(f"Part 2: {get_lowest_risk_path_risk(puzzle_input)}")
