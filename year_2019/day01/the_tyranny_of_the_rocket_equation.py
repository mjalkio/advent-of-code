from util import read_puzzle_input


def get_total_fuel_required(puzzle_input):
    masses = [int(mass) for mass in puzzle_input.split('\n')]
    return sum(mass // 3 - 2 for mass in masses)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_total_fuel_required(puzzle_input)}")
    print(f"Part 2: {get_total_fuel_required(puzzle_input)}")
