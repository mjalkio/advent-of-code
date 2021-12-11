from util import read_puzzle_input


def _parse_input(puzzle_input):
    cmd_lines = [line.split() for line in puzzle_input.split("\n") if line != ""]
    return [(command, int(distance)) for (command, distance) in cmd_lines]


def get_position_product(puzzle_input):
    cmd_lines = _parse_input(puzzle_input)

    position = 0
    depth = 0
    for command, distance in cmd_lines:
        if command == "forward":
            position += distance
        if command == "down":
            depth += distance
        if command == "up":
            depth -= distance
    return position * depth


def get_position_product_with_aim(puzzle_input):
    cmd_lines = _parse_input(puzzle_input)

    position = 0
    depth = 0
    aim = 0
    for command, distance in cmd_lines:
        if command == "forward":
            position += distance
            depth += aim * distance
        if command == "down":
            aim += distance
        if command == "up":
            aim -= distance
    return position * depth


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_position_product(puzzle_input)}")
    print(f"Part 2: {get_position_product_with_aim(puzzle_input)}")
