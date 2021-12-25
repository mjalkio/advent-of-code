from util import read_puzzle_input


def get_num_steps_no_movement(puzzle_input):
    num_steps = 0
    locations = {}
    for y, line in enumerate(puzzle_input.split("\n")):
        for x, char in enumerate(line):
            if char != '.':
                locations[(x, y)] = char
    return num_steps


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_num_steps_no_movement(puzzle_input)}")
    print(f"Part 2: {get_num_steps_no_movement(puzzle_input)}")
