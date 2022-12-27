from util import read_puzzle_input

STARTING_POS = (1, 0)
GOAL_POS = (6, -5)


def _parse_input(puzzle_input):
    blizzards = {}
    for y, line in enumerate(puzzle_input.strip().split("\n")):
        for x in range(len(line)):
            if line[x] != ".":
                blizzards[x, -y] = line[x]
    return blizzards


def _print(blizzards):
    min_x = min(x for x, y in blizzards)
    min_y = min(y for x, y in blizzards)
    max_x = max(x for x, y in blizzards)
    max_y = max(y for x, y in blizzards)

    for y in reversed(range(min_y, max_y + 1)):
        line = ""
        for x in range(min_x, max_x + 1):
            if (x, y) not in blizzards:
                line += "."
            else:
                line += blizzards[x, y]
        print(line)


def num_minutes_to_goal(puzzle_input):
    blizzards = _parse_input(puzzle_input)
    return 0


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {num_minutes_to_goal(puzzle_input)}")
    print(f"Part 2: {num_minutes_to_goal(puzzle_input)}")
