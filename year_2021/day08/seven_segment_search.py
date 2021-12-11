from util import read_puzzle_input


def get_num_easy_digit_outputs(puzzle_input):
    entries = puzzle_input.split('\n')

    num_easy_digits = 0
    for entry in entries:
        unique_patterns, output_digits = [digits.split(' ') for digits in entry.split(' | ')]
        num_easy_digits += sum(len(d) in (2, 3, 4, 7) for d in output_digits)
    return num_easy_digits


def get_outputs_sum(puzzle_input):
    return 0


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_num_easy_digit_outputs(puzzle_input)}")
    print(f"Part 2: {get_outputs_sum(puzzle_input)}")
