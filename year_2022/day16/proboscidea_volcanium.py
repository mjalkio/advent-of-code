import math
from itertools import permutations

from util import read_puzzle_input


STARTING_LOCATION = "AA"
NUM_MINUTES = 30


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

    # Now compute all possible orders to traverse
    all_possible_orders = permutations(
        valve for valve in valves if flow_rates[valve] != 0
    )

    most_pressure_possible = 0
    for order in all_possible_orders:
        pressure_released = 0
        current_location = STARTING_LOCATION
        minute = 1
        i = 0
        while i < len(order) and minute <= NUM_MINUTES:
            minute += distances[current_location, order[i]] + 1
            current_location = order[i]
            if minute > NUM_MINUTES:
                break
            pressure_released += flow_rates[current_location] * (
                NUM_MINUTES - minute + 1
            )
            i += 1
        if pressure_released > most_pressure_possible:
            most_pressure_possible = pressure_released
            print(most_pressure_possible)

    return most_pressure_possible


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {most_pressure_possible(puzzle_input)}")
    print(f"Part 2: {most_pressure_possible(puzzle_input)}")
