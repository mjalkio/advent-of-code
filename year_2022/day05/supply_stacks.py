from util import read_puzzle_input


def get_top_crates(puzzle_input):
    starting_stacks, procedure = puzzle_input.split("\n\n")
    starting_stack_lines = starting_stacks.split("\n")
    num_stacks = len(starting_stack_lines.pop().split("   "))
    return 0


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_top_crates(puzzle_input)}")
    print(f"Part 2: {get_top_crates(puzzle_input)}")
