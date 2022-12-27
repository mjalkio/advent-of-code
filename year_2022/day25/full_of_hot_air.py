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
    num_characters = 1
    max_number = 2
    while max_number < number:
        max_number += 5 ** num_characters * 2
        num_characters += 1
    snafu_number = ""
    current_decimal = 0
    for i in reversed(range(num_characters)):
        remaining_magnitude = sum(5 ** j * 2 for j in range(i))

        if current_decimal + remaining_magnitude < number:
            if current_decimal + remaining_magnitude + 5 ** i >= number:
                snafu_number += "1"
                current_decimal += 5 ** i
                continue
            else:
                snafu_number += "2"
                current_decimal += 5 ** i * 2
                continue

        if current_decimal - remaining_magnitude > number:
            if current_decimal - remaining_magnitude - 5 ** i <= number:
                snafu_number += "-"
                current_decimal -= 5 ** i
                continue
            else:
                snafu_number += "="
                current_decimal -= 5 ** i * 2
                continue

        snafu_number += "0"

    return snafu_number


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {decimal_to_snafu(sum_fuel_requirements(puzzle_input))}")
    print(f"Part 2: {sum_fuel_requirements(puzzle_input)}")
