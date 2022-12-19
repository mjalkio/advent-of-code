import math
from collections import namedtuple

from util import read_puzzle_input


STARTING_LOCATION = "AA"
NUM_MINUTES = 30

Node = namedtuple("Node", ["valve", "pressure_released", "minute", "visited"])


def most_pressure_possible(puzzle_input):
    valves = []
    flow_rates = {}
    tunnels = {}
    for line in puzzle_input.split("\n"):
        words = line.split()
        valve = words[1]
        valves.append(valve)
        flow_rate_desc = words[4]
        flow_rate = int(flow_rate_desc[5:-1])
        flow_rates[valve] = flow_rate
        tunnels[valve] = "".join(words[9:]).split(",")

    # Floyd-Warshall algorithm (or so I hope)
    distances = {}
    for valve1 in valves:
        for valve2 in valves:
            if valve1 == valve2:
                distances[valve1, valve2] = 0
            elif valve2 in tunnels[valve1]:
                distances[valve1, valve2] = 1
            else:
                distances[valve1, valve2] = math.inf
    for k in valves:
        for i in valves:
            for j in valves:
                if distances[i, j] > distances[i, k] + distances[k, j]:
                    distances[i, j] = distances[i, k] + distances[k, j]

    # Depth-first search (DFS)
    useful_valves = set(valve for valve in valves if flow_rates[valve] != 0)
    stack = [
        Node(valve=STARTING_LOCATION, pressure_released=0, minute=1, visited=tuple())
    ]
    most_pressure_possible = 0
    while len(stack) > 0:
        valve, pressure_released, minute, visited = stack.pop()
        for neighbor in useful_valves:
            if (
                neighbor not in visited
                and minute + distances[valve, neighbor] + 1 <= NUM_MINUTES
            ):
                new_time = minute + distances[valve, neighbor] + 1
                stack.append(
                    Node(
                        valve=neighbor,
                        pressure_released=pressure_released
                        + (flow_rates[neighbor] * (NUM_MINUTES - new_time + 1)),
                        minute=new_time,
                        visited=visited + (neighbor,),
                    )
                )
        most_pressure_possible = max(pressure_released, most_pressure_possible)
    return most_pressure_possible


def most_pressure_possible_with_elephant(puzzle_input):
    return 0


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {most_pressure_possible(puzzle_input)}")
    print(f"Part 2: {most_pressure_possible_with_elephant(puzzle_input)}")
