import operator
import os.path as op


def get_input(filename):
    with open(op.join(op.dirname(__file__), filename), 'r') as f:
        puzzle_input = f.read()
    return puzzle_input


def parse_input(puzzle_input):
    reg_op_mapping = {
        'inc': operator.add,
        'dec': operator.sub,
    }
    bool_op_mapping = {
        '>': operator.gt,
        '<': operator.lt,
        '>=': operator.ge,
        '<=': operator.le,
        '!=': operator.ne,
        '==': operator.eq,
    }

    instructions = []
    registers = set()

    for line in puzzle_input.split('\n'):
        line = line.strip()  # trim any whitespace
        register, reg_op, amount, _, bool_reg, bool_op, bool_val = line.split()

        registers.update([register, bool_reg])

        instruction = (
            register,
            reg_op_mapping[reg_op],
            int(amount),
            bool_reg,
            bool_op_mapping[bool_op],
            int(bool_val),
        )
        instructions.append(instruction)

    return instructions, registers


def get_largest_register_value(puzzle_input):
    instructions, register_names = parse_input(puzzle_input)
    registers = {reg: 0 for reg in register_names}
    for instruction in instructions:
        register, reg_op, amount, bool_reg, bool_op, bool_val = instruction
        if bool_op(registers[bool_reg], bool_val):
            registers[register] = reg_op(registers[register], amount)
    return max(registers.values())
