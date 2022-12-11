from util import read_puzzle_input


def sum_interesting_signal_strengths(puzzle_input):
    instructions = [line for line in puzzle_input.split("\n") if line != ""]
    cycle_value = 1
    X = 1
    signal_strengths = []
    for instr in instructions:
        signal_strengths.append(cycle_value * X)
        if instr == "noop":
            cycle_value += 1
        else:
            V = int(instr[5:])
            cycle_value += 1
            signal_strengths.append(cycle_value * X)
            X += V
            cycle_value += 1
    return sum(
        signal_strengths[i] for i in range(len(signal_strengths)) if (i - 19) % 40 == 0
    )


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {sum_interesting_signal_strengths(puzzle_input)}")
    print(f"Part 2: {sum_interesting_signal_strengths(puzzle_input)}")
