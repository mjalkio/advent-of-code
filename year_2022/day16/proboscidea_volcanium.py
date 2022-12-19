import math
from collections import namedtuple

from util import read_puzzle_input


STARTING_LOCATION = "AA"
NUM_MINUTES = 30
NUM_MINUTES_WITH_ELEPHANT = 26

Node = namedtuple("Node", ["valve", "pressure_released", "minute", "visited"])


def _parse_input(puzzle_input):
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
    return valves, flow_rates, tunnels


def _get_distances(valves, tunnels):
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
    return distances


def most_pressure_possible(puzzle_input):
    valves, flow_rates, tunnels = _parse_input(puzzle_input)
    distances = _get_distances(valves, tunnels)

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
    valves, flow_rates, tunnels = _parse_input(puzzle_input)
    distances = _get_distances(valves, tunnels)

    # Depth-first search (DFS)
    plan_values = {}
    useful_valves = set(valve for valve in valves if flow_rates[valve] != 0)
    stack = [
        Node(valve=STARTING_LOCATION, pressure_released=0, minute=1, visited=tuple())
    ]
    while len(stack) > 0:
        valve, pressure_released, minute, visited = stack.pop()
        for neighbor in useful_valves:
            if (
                neighbor not in visited
                and minute + distances[valve, neighbor] + 1 <= NUM_MINUTES_WITH_ELEPHANT
            ):
                new_time = minute + distances[valve, neighbor] + 1
                stack.append(
                    Node(
                        valve=neighbor,
                        pressure_released=pressure_released
                        + (
                            flow_rates[neighbor]
                            * (NUM_MINUTES_WITH_ELEPHANT - new_time + 1)
                        ),
                        minute=new_time,
                        visited=visited + (neighbor,),
                    )
                )
        plan_values[visited] = pressure_released

    most_pressure_possible = 0
    print(f"Total of {len(plan_values)} plans to consider.")
    sorted_plan_values = sorted(plan_values.items(), key=lambda a: a[1], reverse=True)
    for i, (plan_a, plan_a_pressure) in enumerate(sorted_plan_values):
        if i % 1_000 == 0:
            print(f"Computed pressure of {i / len(plan_values) * 100}% plans...")
        for plan_b, plan_b_pressure in sorted_plan_values:
            if len(set(plan_a).intersection(set(plan_b))) == 0:
                total_pressure = plan_a_pressure + plan_b_pressure
                if total_pressure > most_pressure_possible:
                    print(f"Best pressure found so far: {total_pressure}")
                    most_pressure_possible = total_pressure
    return most_pressure_possible


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {most_pressure_possible(puzzle_input)}")
    print(f"Part 2: {most_pressure_possible_with_elephant(puzzle_input)}")
