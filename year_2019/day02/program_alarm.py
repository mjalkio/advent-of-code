from math import prod

from util import read_puzzle_input


def run_intcode_program(program):
    memory = [int(address) for address in program.split(",")]
    ins_ptr = 0
    while memory[ins_ptr] != 99:
        if memory[ins_ptr] not in (1, 2):
            raise ValueError("Unexpected opcode.")

        if memory[ins_ptr] == 1:
            operation = sum
        if memory[ins_ptr] == 2:
            operation = prod
        output_address = memory[ins_ptr + 3]
        operand_addresses = (memory[ins_ptr + 1], memory[ins_ptr + 2])
        operands = (memory[add] for add in operand_addresses)
        memory[output_address] = operation(operands)
        ins_ptr += 4
    return ",".join(str(address) for address in memory)


def restore_gravity_assist(puzzle_input):
    memory = [int(address) for address in puzzle_input.split(",")]
    memory[1] = 12
    memory[2] = 2
    program = ",".join(str(address) for address in memory)
    return run_intcode_program(program).split(",")[0]


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {restore_gravity_assist(puzzle_input)}")
    print(f"Part 2: {restore_gravity_assist(puzzle_input)}")
