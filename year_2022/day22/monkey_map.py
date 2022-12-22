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


def _step(pos, board):
    x, y, facing = pos
    potential_new_positions = {
        FACING[RIGHT]: (x + 1, y),
        FACING[LEFT]: (x - 1, y),
        FACING[DOWN]: (x, y + 1),
        FACING[UP]: (x, y - 1),
    }
    potential_pos = potential_new_positions[facing]
    if potential_pos not in board:
        # Wrap around
        if facing in (FACING[RIGHT], FACING[DOWN]):
            wrap_func = min
        else:
            wrap_func = max

        if facing in (FACING[UP], FACING[DOWN]):
            potential_pos = (
                x,
                wrap_func(wrap_y for wrap_x, wrap_y in board if wrap_x == x),
            )
        else:
            potential_pos = (
                wrap_func(wrap_x for wrap_x, wrap_y in board if wrap_y == y),
                y,
            )

    if board[potential_pos] == SOLID_WALL:
        return pos
    else:
        return Position(x=potential_pos[0], y=potential_pos[1], facing=facing)


def final_password(puzzle_input):
    board, path = _parse_input(puzzle_input)
    pos = Position(
        x=min(x for x, y in board if board[x, y] == OPEN_TILE and y == STARTING_Y),
        y=STARTING_Y,
        facing=FACING[RIGHT],
    )

    for step in path:
        if isinstance(step, int):
            for _ in range(step):
                pos = _step(pos, board)
            continue

        facing = pos.facing
        if step == RIGHT:
            facing += 1
        elif step == LEFT:
            facing -= 1
        facing = facing % len(FACING)
        pos = Position(x=pos.x, y=pos.y, facing=facing)
    return 1000 * pos.y + 4 * pos.x + pos.facing


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {final_password(puzzle_input)}")
    print(f"Part 2: {final_password(puzzle_input)}")
