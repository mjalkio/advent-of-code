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
    return 0


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {most_pressure_possible(puzzle_input)}")
    print(f"Part 2: {most_pressure_possible(puzzle_input)}")
