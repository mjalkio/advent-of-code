from collections import defaultdict

from util import read_puzzle_input

GROUND = "."
WALL = "#"

UP = "^"
DOWN = "v"
LEFT = "<"
RIGHT = ">"


def _parse_input(puzzle_input):
    grid = defaultdict(str)
    for y, line in enumerate(puzzle_input.strip().split("\n")):
        for x in range(len(line)):
            grid[x, -y] = line[x]
    return grid


def _print(grid):
    min_x = min(x for x, y in grid)
    min_y = min(y for x, y in grid)
    max_x = max(x for x, y in grid)
    max_y = max(y for x, y in grid)

    for y in reversed(range(min_y, max_y + 1)):
        line = ""
        for x in range(min_x, max_x + 1):
            if len(grid[x, y]) > 1:
                line += str(len(grid[x, y]))
            else:
                line += grid[x, y][0]
        print(line)


def _move(grid):
    min_x = min(x for x, y in grid) + 1
    min_y = min(y for x, y in grid) + 1
    max_x = max(x for x, y in grid) - 1
    max_y = max(y for x, y in grid) - 1

    new_grid = defaultdict(str)
    for (x, y) in grid:
        if grid[x, y] == WALL:
            new_grid[x, y] = WALL
            continue

        if y < min_y or y > max_y:
            # Start point and goal point
            assert grid[x, y] == GROUND
            new_grid[x, y] = GROUND

        for b in grid[x, y]:
            if b == UP:
                if grid[x, y + 1] == WALL:
                    new_grid[x, min_y] += b
                else:
                    new_grid[x, y + 1] += b

            if b == DOWN:
                if grid[x, y - 1] == WALL:
                    new_grid[x, max_y] += b
                else:
                    new_grid[x, y - 1] += b

            if b == RIGHT:
                if grid[x + 1, y] == WALL:
                    new_grid[min_x, y] += b
                else:
                    new_grid[x + 1, y] += b

            if b == LEFT:
                if grid[x - 1, y] == WALL:
                    new_grid[max_x, y] += b
                else:
                    new_grid[x - 1, y] += b

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if (x, y) not in new_grid:
                new_grid[x, y] = GROUND

    return new_grid


def num_minutes_to_goal(puzzle_input):
    grid = _parse_input(puzzle_input)
    new_grid = _move(grid)
    return new_grid


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {num_minutes_to_goal(puzzle_input)}")
    print(f"Part 2: {num_minutes_to_goal(puzzle_input)}")
