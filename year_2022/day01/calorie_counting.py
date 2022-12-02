from util import read_puzzle_input


def _get_elf_snack_calories(puzzle_input):
    elf_snack_calorie_lines = puzzle_input.split("\n\n")
    elf_snack_calories = []
    for line in elf_snack_calorie_lines:
        snack_calories = [int(cal) for cal in line.split("\n")]
        elf_snack_calories.append(snack_calories)
    return elf_snack_calories


def get_max_total_calories(puzzle_input):
    elf_snack_calories = _get_elf_snack_calories(puzzle_input)
    return max([sum(cals) for cals in elf_snack_calories])


def get_top_three_total_calories(puzzle_input):
    elf_snack_calories = _get_elf_snack_calories(puzzle_input)
    sorted_total_calories = sorted([sum(cals) for cals in elf_snack_calories])
    return sum(list(sorted_total_calories)[-3:])


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_max_total_calories(puzzle_input)}")
    print(f"Part 2: {get_top_three_total_calories(puzzle_input)}")
