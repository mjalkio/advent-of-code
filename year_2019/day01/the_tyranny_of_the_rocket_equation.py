from util import read_puzzle_input


def get_total_fuel_required(puzzle_input):
    masses = [int(mass) for mass in puzzle_input.split('\n')]
    return sum(mass // 3 - 2 for mass in masses)


def get_total_fuel_required_double_check(puzzle_input):
    masses = [int(mass) for mass in puzzle_input.split('\n')]
    initial_fuel_requirements = [mass // 3 - 2 for mass in masses]
    total_fuel = 0
    for fuel in initial_fuel_requirements:
        while fuel > 0:
            total_fuel += fuel
            fuel = fuel // 3 - 2
    return total_fuel


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_total_fuel_required(puzzle_input)}")
    print(f"Part 2: {get_total_fuel_required_double_check(puzzle_input)}")
