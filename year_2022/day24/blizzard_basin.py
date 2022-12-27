from collections import defaultdict

from util import read_puzzle_input

STARTING_POS = (1, 0)
GOAL_POS = (6, -5)

WALL = "#"

UP = "^"
DOWN = "v"
LEFT = "<"
RIGHT = ">"


def _parse_input(puzzle_input):
    blizzards = defaultdict(str)
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
            elif len(blizzards[x, y]) > 1:
                line += str(len(blizzards[x, y]))
            else:
                line += blizzards[x, y][0]
        print(line)


def _move(blizzards):
    min_x = min(x for x, y in blizzards if blizzards[x, y] != WALL)
    min_y = min(y for x, y in blizzards if blizzards[x, y] != WALL)
    max_x = max(x for x, y in blizzards if blizzards[x, y] != WALL)
    max_y = max(y for x, y in blizzards if blizzards[x, y] != WALL)

    new_blizzards = defaultdict(str)
    for (x, y) in blizzards:
        if blizzards[x, y] == WALL:
            new_blizzards[x, y] = WALL
            continue

        for b in blizzards[x, y]:
            if b == UP:
                if blizzards[x, y + 1] == WALL:
                    new_blizzards[x, min_y] += b
                else:
                    new_blizzards[x, y + 1] += b

            if b == DOWN:
                if blizzards[x, y - 1] == WALL:
                    new_blizzards[x, max_y] += b
                else:
                    new_blizzards[x, y - 1] += b

            if b == RIGHT:
                if blizzards[x + 1, y] == WALL:
                    new_blizzards[min_x, y] += b
                else:
                    new_blizzards[x + 1, y] += b

            if b == LEFT:
                if blizzards[x - 1, y] == WALL:
                    new_blizzards[max_x, y] += b
                else:
                    new_blizzards[x - 1, y] += b

    return new_blizzards


def num_minutes_to_goal(puzzle_input):
    blizzards = _parse_input(puzzle_input)
    new_blizzards = _move(blizzards)
    return new_blizzards


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {num_minutes_to_goal(puzzle_input)}")
    print(f"Part 2: {num_minutes_to_goal(puzzle_input)}")
