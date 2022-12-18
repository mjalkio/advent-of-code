import math

from util import read_puzzle_input


def most_pressure_possible(puzzle_input):
    flow_rates = {}
    tunnels = {}
    for line in puzzle_input.split("\n"):
        words = line.split()
        valve = words[1]
        flow_rate_desc = words[4]
        flow_rate = int(flow_rate_desc[5:-1])
        flow_rates[valve] = flow_rate
        tunnels[valve] = "".join(words[9:]).split(",")

    # Floyd-Warshall algorithm (or so I hope)
    distances = {}
    for valve1 in flow_rates.keys():
        for valve2 in flow_rates.keys():
            if valve1 == valve2:
                distances[valve1, valve2] = 0
            elif valve2 in tunnels[valve1]:
                distances[valve1, valve2] = 1
            else:
                distances[valve1, valve2] = math.inf
    for k in flow_rates.keys():
        for i in flow_rates.keys():
            for j in flow_rates.keys():
                if distances[i, j] > distances[i, k] + distances[k, j]:
                    distances[i, j] = distances[i, k] + distances[k, j]
    return 0


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {most_pressure_possible(puzzle_input)}")
    print(f"Part 2: {most_pressure_possible(puzzle_input)}")
