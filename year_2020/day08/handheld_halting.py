from util import read_puzzle_input


def _parse_instruction(instruction_line):
    operation, argument = instruction_line.split()
    return (operation, int(argument[1:]) if argument[0] == '+' else -1 * int(argument[1:]))


def get_acc_at_infinite_loop_start(puzzle_input):
    instructions = [
        _parse_instruction(line)
        for line
        in puzzle_input.split('\n')
        if line != ''
    ]
    accumulator = 0
    curr_instruction = 0
    visited_instructions = set()
    while curr_instruction not in visited_instructions:
        visited_instructions.add(curr_instruction)

        operation, argument = instructions[curr_instruction]
        if operation == 'jmp':
            curr_instruction += argument
            continue

        if operation == 'acc':
            accumulator += argument
        curr_instruction += 1

    return accumulator


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_acc_at_infinite_loop_start(puzzle_input)}")
    print(f"Part 2: {None}")
