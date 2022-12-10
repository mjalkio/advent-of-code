from util import read_puzzle_input


def num_positions_tail_visits(puzzle_input):
    tail_positions = set()
    steps = []
    for line in puzzle_input.split("\n"):
        if line == "":
            continue
        direction, num_steps = line.split()
        steps += [direction] * int(num_steps)
    return len(tail_positions)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {num_positions_tail_visits(puzzle_input)}")
    print(f"Part 2: {num_positions_tail_visits(puzzle_input)}")
