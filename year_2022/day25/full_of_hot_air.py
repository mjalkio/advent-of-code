from util import read_puzzle_input


def sum_fuel_requirements(puzzle_input):
    snafu_nums = puzzle_input.strip().split("\n")
    return sum(snafu_to_decimal(num) for num in snafu_nums)


def snafu_to_decimal(number):
    return 0


def decimal_to_snafu(number):
    return ""


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {decimal_to_snafu(sum_fuel_requirements(puzzle_input))}")
    print(f"Part 2: {sum_fuel_requirements(puzzle_input)}")
