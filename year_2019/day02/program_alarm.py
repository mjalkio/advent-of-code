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


def get_position_after_run(puzzle_input, position):
    return run_intcode_program(puzzle_input)[position]


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_position_after_run(puzzle_input, 0)}")
    print(f"Part 2: {get_position_after_run(puzzle_input, 0)}")
