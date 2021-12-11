import os.path as op


def get_instructions():
    with open(op.join(op.dirname(__file__), "puzzle_input.txt"), "r") as f:
        puzzle_input = f.read()
    return [int(instruction) for instruction in puzzle_input.split("\n")]


def num_jumps(instructions):
    location = 0
    num_jumps = 0
    while location >= 0 and location < len(instructions):
        num_jumps += 1
        instructions[location] += 1
        location += instructions[location] - 1

    return num_jumps


if __name__ == "__main__":
    instructions = get_instructions()
    print(num_jumps(instructions))
