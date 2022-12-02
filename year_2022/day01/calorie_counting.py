from util import read_puzzle_input


def get_max_total_calories(puzzle_input):
    elf_snack_calorie_lines = puzzle_input.split("\n\n")
    elf_snack_calories = []
    for line in elf_snack_calorie_lines:
        snack_calories = [int(cal) for cal in line.split("\n")]
        elf_snack_calories.append(snack_calories)
    return max([sum(cals) for cals in elf_snack_calories])


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_max_total_calories(puzzle_input)}")
    print(f"Part 2: {get_max_total_calories(puzzle_input)}")
