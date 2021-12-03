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
    lines = puzzle_input.split()
    oxygen_rating_candidates = list(lines)
    c02_rating_candidates = list(lines)

    for i in range(len(oxygen_rating_candidates[0])):
        if len(oxygen_rating_candidates) == 1:
            break

        oxygen_bits = [num[i] for num in oxygen_rating_candidates]
        oxygen_counts = Counter(oxygen_bits)
        if oxygen_counts['1'] >= oxygen_counts['0']:
            most_common_val = '1'
        else:
            most_common_val = '0'
        oxygen_rating_candidates = [
            num
            for num
            in oxygen_rating_candidates
            if num[i] == most_common_val
        ]

    for i in range(len(c02_rating_candidates[0])):
        if len(c02_rating_candidates) == 1:
            break

        c02_bits = [num[i] for num in c02_rating_candidates]
        c02_counts = Counter(c02_bits)
        if c02_counts['1'] >= c02_counts['0']:
            least_common_val = '0'
        else:
            least_common_val = '1'
        c02_rating_candidates = [
            num
            for num
            in c02_rating_candidates
            if num[i] == least_common_val
        ]

    oxygen_generator_rating = oxygen_rating_candidates[0]
    c02_scrubber_rating = c02_rating_candidates[0]
    return int(oxygen_generator_rating, 2) * int(c02_scrubber_rating, 2)


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_power_consumption(puzzle_input)}")
    print(f"Part 2: {get_life_support_rating(puzzle_input)}")
