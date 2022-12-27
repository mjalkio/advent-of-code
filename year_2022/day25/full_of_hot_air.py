from util import read_puzzle_input


SNAFU_MAP = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2,
}


def sum_fuel_requirements(puzzle_input):
    snafu_nums = puzzle_input.strip().split("\n")
    return sum(snafu_to_decimal(num) for num in snafu_nums)


def snafu_to_decimal(number):
    decimal_number = 0
    for i, char in enumerate(reversed(number)):
        decimal_number += 5 ** i * SNAFU_MAP[char]
    return decimal_number


def decimal_to_snafu(number):
    return ""


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {decimal_to_snafu(sum_fuel_requirements(puzzle_input))}")
    print(f"Part 2: {sum_fuel_requirements(puzzle_input)}")
