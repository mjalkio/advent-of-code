from math import prod

from util import read_puzzle_input


def run_intcode_program(program):
    integers = [int(i) for i in program.split(",")]
    i = 0
    while integers[i] != 99:
        if integers[i] not in (1, 2):
            raise ValueError("Unexpected opcode.")

        if integers[i] == 1:
            operation = sum
        if integers[i] == 2:
            operation = prod
        output_idx = integers[i + 3]
        operand_indices = (integers[i + 1], integers[i + 2])
        operands = (integers[idx] for idx in operand_indices)
        integers[output_idx] = operation(operands)
        i += 4
    return ",".join(str(i) for i in integers)


def restore_gravity_assist(puzzle_input):
    integers = [int(i) for i in puzzle_input.split(",")]
    integers[1] = 12
    integers[2] = 2
    program = ",".join(str(i) for i in integers)
    return run_intcode_program(program).split(",")[0]


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {restore_gravity_assist(puzzle_input)}")
    print(f"Part 2: {restore_gravity_assist(puzzle_input)}")
