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
        num_characters += 1
        max_number += 5 ** num_characters
    snafu_number = ""
    current_decimal = 0
    for i in reversed(range(num_characters)):
        character_found = False
        amount_could_subtract = sum(5 ** j * -2 for j in range(i))
        amount_could_add = sum(5 ** j * 2 for j in range(i))

        for snafu_char in ("=", "-"):
            if (
                current_decimal + (5 ** i * SNAFU_MAP[snafu_char]) + amount_could_add
                >= number
                and not character_found
            ):
                snafu_number += snafu_char
                character_found = True

        for snafu_char in ("2", "1"):
            if (
                current_decimal
                + (5 ** i * SNAFU_MAP[snafu_char])
                - amount_could_subtract
                <= number
                and not character_found
            ):
                snafu_number += snafu_char
                character_found = True

        if not character_found:
            snafu_number += "0"
    return snafu_number


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {decimal_to_snafu(sum_fuel_requirements(puzzle_input))}")
    print(f"Part 2: {sum_fuel_requirements(puzzle_input)}")
