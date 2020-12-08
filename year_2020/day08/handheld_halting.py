from util import read_puzzle_input


def _parse_instruction(instruction_line):
    operation, argument = instruction_line.split()
    return (operation, int(argument[1:]) if argument[0] == '+' else -1 * int(argument[1:]))


def _parse_input(puzzle_input):
    return [
        _parse_instruction(line)
        for line
        in puzzle_input.split('\n')
        if line != ''
    ]


def _run_program(instructions):
    accumulator = 0
    curr_instruction = 0
    visited_instructions = set()
    while curr_instruction not in visited_instructions:
        if curr_instruction >= len(instructions):
            return True, accumulator

        visited_instructions.add(curr_instruction)

        operation, argument = instructions[curr_instruction]
        if operation == 'jmp':
            curr_instruction += argument
            continue

        if operation == 'acc':
            accumulator += argument
        curr_instruction += 1

    return False, accumulator


def get_acc_at_infinite_loop_start(puzzle_input):
    instructions = _parse_input(puzzle_input)
    _, accumulator = _run_program(instructions)
    return accumulator


def get_acc_at_program_termination(puzzle_input):
    instructions = _parse_input(puzzle_input)
    for i, (operation, argument) in enumerate(instructions):
        if operation == 'acc':
            continue

        modified_instructions = list(instructions)
        if operation == 'jmp':
            modified_instructions[i] = ('nop', argument)
        else:
            modified_instructions[i] = ('jmp', argument)
        terminated, accumulator = _run_program(modified_instructions)

        if terminated:
            return accumulator

    raise ValueError('I am Zardoz')


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_acc_at_infinite_loop_start(puzzle_input)}")
    print(f"Part 2: {get_acc_at_program_termination(puzzle_input)}")
