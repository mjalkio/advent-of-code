from util import read_puzzle_input


def get_top_crates(puzzle_input):
    starting_stacks, procedure = puzzle_input.split("\n\n")

    starting_stack_lines = starting_stacks.split("\n")
    num_stacks = len(starting_stack_lines.pop().split("   "))
    stacks = []
    for _ in range(num_stacks):
        stacks.append([])

    for line in starting_stack_lines:
        i = 0
        while len(line) > 0:
            crate, line = line[1], line[4:]
            if crate != " ":
                stacks[i].append(crate)
            i += 1
    for stack in stacks:
        stack.reverse()

    return 0


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_top_crates(puzzle_input)}")
    print(f"Part 2: {get_top_crates(puzzle_input)}")
