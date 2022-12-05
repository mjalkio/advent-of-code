from util import read_puzzle_input


def get_top_crates(puzzle_input, cratemover_model="9000"):
    starting_stacks, procedure = puzzle_input.split("\n\n")

    starting_stack_lines = starting_stacks.split("\n")
    num_stacks = len(starting_stack_lines.pop().split("   "))
    stacks = []
    for _ in range(num_stacks):
        stacks.append([])

    for level in starting_stack_lines:
        i = 0
        while len(level) > 0:
            crate, level = level[1], level[4:]
            if crate != " ":
                stacks[i].append(crate)
            i += 1
    for stack in stacks:
        stack.reverse()

    for step in procedure.split("\n"):
        move_instr, stack_instr = step.split(" from ")
        num_move = int(move_instr[5:])
        from_stack, to_stack = [
            int(stack_idx) - 1 for stack_idx in stack_instr.split(" to ")
        ]

        if cratemover_model == "9000":
            for _ in range(num_move):
                moved_crate = stacks[from_stack].pop()
                stacks[to_stack].append(moved_crate)
        elif cratemover_model == "9001":
            moved_crates = stacks[from_stack][-num_move:]
            stacks[from_stack] = stacks[from_stack][:-num_move]
            stacks[to_stack] = stacks[to_stack] + moved_crates
        else:
            raise ValueError(f"Unsupported CrateMover model: {cratemover_model}")

    top_crates = [stack[-1] for stack in stacks]
    return "".join(top_crates)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_top_crates(puzzle_input)}")
    print(f"Part 2: {get_top_crates(puzzle_input, cratemover_model='9001')}")
