from util import read_puzzle_input


def get_fuel_spent(puzzle_input):
    positions = [int(pos) for pos in puzzle_input.split(',')]
    least_fuel_spent = None
    for possible_pos in range(min(positions), max(positions) + 1):
        fuel_spent = 0
        for pos in positions:
            fuel_spent += abs(pos - possible_pos)
        if least_fuel_spent is None or fuel_spent < least_fuel_spent:
            least_fuel_spent = fuel_spent
    return least_fuel_spent


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_fuel_spent(puzzle_input)}")
    print(f"Part 2: {get_fuel_spent(puzzle_input)}")
