def num_jumps(instructions):
    location = 0
    num_jumps = 0
    while location >= 0 and location < len(instructions):
        num_jumps += 1
        instructions[location] += 1
        location += instructions[location] - 1

    return num_jumps
