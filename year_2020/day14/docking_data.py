from util import read_puzzle_input

MASK_PREFIX = 'mask = '


def get_masked_address(value, mask):
    binary_value = bin(value)[2:].zfill(len(mask))
    masked_value_bits = []
    for i in range(len(mask)):
        if mask[i] == '0':
            masked_value_bits.append(binary_value[i])
        elif mask[i] == '1':
            masked_value_bits.append('1')
        else:
            masked_value_bits.append('X')
    return ''.join(masked_value_bits)


def get_masked_value(value, mask):
    binary_value = bin(value)[2:].zfill(len(mask))
    masked_value_bits = []
    for i in range(len(mask)):
        if mask[i] == 'X':
            masked_value_bits.append(binary_value[i])
        else:
            masked_value_bits.append(mask[i])
    return int(''.join(masked_value_bits), base=2)


def _get_memory_locations_for_masked_address(masked_address):
    first_bit = masked_address[0]
    if first_bit in ('1', '0'):
        memory_locations = [[first_bit]]
    else:
        memory_locations = [['1'], ['0']]

    for bit in masked_address[1:]:
        if bit in ('1', '0'):
            for memory_location in memory_locations:
                if memory_location is None:
                    import pdb; pdb.set_trace()
                memory_location.append(bit)
            continue

        new_memory_locations = []
        for memory_location in memory_locations:
            new_memory_locations.append(memory_location + ['1'])
            new_memory_locations.append(memory_location + ['0'])
        memory_locations = new_memory_locations
    return [int(''.join(loc), base=2) for loc in memory_locations]


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
        if use_version_2:
            masked_address = get_masked_address(value=mem_location, mask=mask)
            mem_locations_to_update = _get_memory_locations_for_masked_address(masked_address)
            for ml in mem_locations_to_update:
                memory[ml] = int(value)
        else:
            memory[mem_location] = get_masked_value(value=int(value), mask=mask)
    return sum(memory.values())


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_memory_sum(puzzle_input)}")
    print(f"Part 2: {get_memory_sum(puzzle_input, use_version_2=True)}")
