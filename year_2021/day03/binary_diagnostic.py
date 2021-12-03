from collections import Counter

from util import read_puzzle_input


def get_power_consumption(puzzle_input):
    lines = puzzle_input.split()
    bits_by_position = []
    for i in range(len(lines[0])):
        bits_by_position.append([num[i] for num in lines])

    gamma_rate = ''
    epsilon_rate = ''
    for bits in bits_by_position:
        counts = Counter(bits)
        if counts['1'] > counts['0']:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def get_life_support_rating(puzzle_input):
    return 0


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_power_consumption(puzzle_input)}")
    print(f"Part 2: {get_life_support_rating(puzzle_input)}")
