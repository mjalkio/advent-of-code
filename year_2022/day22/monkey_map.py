from collections import namedtuple

from util import read_puzzle_input

RIGHT = "R"
LEFT = "L"
UP = "^"
DOWN = "v"

OPEN_TILE = "."
SOLID_WALL = "#"

STARTING_Y = 1

FACING = {
    RIGHT: 0,
    DOWN: 1,
    LEFT: 2,
    UP: 3,
}

Position = namedtuple("Position", ["x", "y", "facing"])


def _parse_input(puzzle_input):
    board, path = puzzle_input.split("\n\n")
    board_map = {}
    for y, line in enumerate(board.split("\n")):
        for x in range(len(line)):
            if line[x] != " ":
                board_map[x + 1, y + 1] = line[x]

    path_lst = []
    while len(path) > 0:
        if LEFT not in path and RIGHT not in path:
            path_lst.append(int(path))
            path = ""
        else:
            for i in range(len(path)):
                if path[i] in (LEFT, RIGHT):
                    path_lst.append(int(path[:i]))
                    path_lst.append(path[i])
                    path = path[i + 1 :]
                    break

    return board_map, path_lst


def final_password(puzzle_input):
    board, path = _parse_input(puzzle_input)
    pos = Position(
        x=min(x for x, y in board if board[x, y] == OPEN_TILE and y == STARTING_Y),
        y=STARTING_Y,
        facing=FACING[RIGHT],
    )
    return 1000 * pos.y + 4 * pos.x + pos.facing


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {final_password(puzzle_input)}")
    print(f"Part 2: {final_password(puzzle_input)}")
