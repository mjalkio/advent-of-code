from util import read_puzzle_input


def get_masked_value(value, mask):
    binary_value = bin(value)[2:].zfill(len(mask))
    masked_value_bits = []
    for i in range(len(mask)):
        if mask[i] == 'X':
            masked_value_bits.append(binary_value[i])
        else:
            masked_value_bits.append(mask[i])
    return int(''.join(masked_value_bits), base=2)


def get_memory_sum(puzzle_input):
    return None


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_memory_sum(puzzle_input)}")
    print(f"Part 2: {None}")
