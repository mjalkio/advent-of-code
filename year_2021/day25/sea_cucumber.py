from util import read_puzzle_input


EAST = ">"
SOUTH = "v"


def get_num_steps_no_movement(puzzle_input):
    num_steps = 0
    locations = {}
    for y, line in enumerate(puzzle_input.split("\n")):
        for x, char in enumerate(line):
            if char != ".":
                locations[(x, y)] = char
    x_wrap = x + 1
    y_wrap = y + 1

    while True:
        num_steps += 1

        east_movers = set()
        for (x, y), cucumber in locations.items():
            if cucumber == SOUTH:
                continue
            if ((x + 1) % x_wrap, y) not in locations:
                east_movers.add((x, y))

        for x, y in east_movers:
            del locations[(x, y)]
            locations[((x + 1) % x_wrap, y)] = EAST

        south_movers = set()
        for (x, y), cucumber in locations.items():
            if cucumber == EAST:
                continue
            if (x, (y + 1) % y_wrap) not in locations:
                south_movers.add((x, y))

        for x, y in south_movers:
            del locations[(x, y)]
            locations[(x, (y + 1) % y_wrap)] = SOUTH

        if len(east_movers) == 0 and len(south_movers) == 0:
            return num_steps


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_num_steps_no_movement(puzzle_input)}")
    print(f"Part 2: {get_num_steps_no_movement(puzzle_input)}")
