from day5part1 import get_instructions


def num_jumps_again(instructions):
    location = 0
    num_jumps = 0
    while location >= 0 and location < len(instructions):
        num_jumps += 1
        new_location = location + instructions[location]
        if instructions[location] >= 3:
            instructions[location] -= 1
        else:
            instructions[location] += 1
        location = new_location

    return num_jumps


if __name__ == '__main__':
    instructions = get_instructions()
    print(num_jumps_again(instructions))
