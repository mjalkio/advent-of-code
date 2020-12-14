from util import read_puzzle_input

MASK_PREFIX = 'mask = '


def get_masked_address(value, mask):
    return None


def get_masked_value(value, mask):
    binary_value = bin(value)[2:].zfill(len(mask))
    masked_value_bits = []
    for i in range(len(mask)):
        if mask[i] == 'X':
            masked_value_bits.append(binary_value[i])
        else:
            masked_value_bits.append(mask[i])
    return int(''.join(masked_value_bits), base=2)


def get_memory_sum(puzzle_input, use_version_2=False):
    initialization_program = [line for line in puzzle_input.split('\n') if line != '']
    memory = {}
    mask = None
    for line in initialization_program:
        if line.startswith(MASK_PREFIX):
            mask = line.replace(MASK_PREFIX, '')
            continue
        mem_instruction, value = line.split(' = ')
        # Instructions are of the form mem[XXX]
        mem_location = int(mem_instruction[4:-1])
        memory[mem_location] = get_masked_value(value=int(value), mask=mask)
    return sum(memory.values())


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_memory_sum(puzzle_input)}")
    print(f"Part 2: {get_memory_sum(puzzle_input, use_version_2=True)}")
