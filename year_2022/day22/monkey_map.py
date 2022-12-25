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


def _wrap_2d(pos, board):
    x, y, facing = pos
    if facing in (FACING[RIGHT], FACING[DOWN]):
        wrap_func = min
    else:
        wrap_func = max

    if facing in (FACING[UP], FACING[DOWN]):
        return (
            x,
            wrap_func(wrap_y for wrap_x, wrap_y in board if wrap_x == x),
            facing,
        )
    else:
        return (
            wrap_func(wrap_x for wrap_x, wrap_y in board if wrap_y == y),
            y,
            facing,
        )


def _wrap_cube(pos, board):
    if pos.y == 1 and pos.facing == FACING[UP] and pos.x in range(51, 101):
        # 2 -> 6
        return Position(x=1, y=pos.x + 100, facing=FACING[RIGHT])
    if pos.x == 1 and pos.facing == FACING[LEFT] and pos.y in range(151, 201):
        # 6 -> 2
        return Position(x=pos.y - 100, y=1, facing=FACING[DOWN])

    if pos.x == 51 and pos.facing == FACING[LEFT] and pos.y in range(1, 51):
        # 2 -> 5
        return Position(x=1, y=151 - pos.y, facing=FACING[RIGHT])
    if pos.x == 1 and pos.facing == FACING[LEFT] and pos.y in range(101, 151):
        # 5 -> 2
        return Position(x=51, y=51 - (pos.y - 100), facing=FACING[DOWN])

    if pos.y == 200 and pos.facing == FACING[DOWN] and pos.x in range(1, 51):
        # 6 -> 1
        return Position(x=100 + pos.x, y=1, facing=FACING[DOWN])
    if pos.y == 1 and pos.facing == FACING[UP] and pos.x in range(101, 151):
        # 1 -> 6
        return Position(x=pos.x - 100, y=200, facing=FACING[UP])

    if pos.x == 100 and pos.facing == FACING[RIGHT] and pos.y in range(51, 101):
        # 3 -> 1
        return Position(x=pos.y + 50, y=50, facing=FACING[UP])
    if pos.y == 50 and pos.facing == FACING[DOWN] and pos.x in range(101, 151):
        # 1 -> 3
        return Position(x=100, y=50 + (pos.x - 100), facing=FACING[LEFT])

    if pos.x == 150 and pos.facing == FACING[RIGHT] and pos.y in range(1, 51):
        # 1 -> 4
        return Position(x=100, y=151 - pos.y, facing=FACING[LEFT])
    if pos.x == 100 and pos.facing == FACING[RIGHT] and pos.y in range(101, 151):
        # 4 -> 1
        return Position(x=150, y=51 - (pos.y - 100), facing=FACING[LEFT])

    if pos.x == 51 and pos.facing == FACING[LEFT] and pos.y in range(51, 101):
        # 3 -> 5
        return Position(x=pos.y - 50, y=101, facing=FACING[DOWN])
    if pos.y == 101 and pos.facing == FACING[UP] and pos.x in range(1, 51):
        # 5 -> 3
        return Position(x=51, y=50 + pos.x, facing=FACING[RIGHT])

    if pos.y == 150 and pos.facing == FACING[DOWN] and pos.x in range(51, 101):
        # 4 -> 6
        return Position(x=50, y=100 + pos.x, facing=FACING[LEFT])
    if pos.x == 50 and pos.facing == FACING[RIGHT] and pos.y in range(151, 201):
        # 6 -> 4
        return Position(x=pos.y - 100, y=150, facing=FACING[UP])


def _wrap(pos, board, is_cube):
    if is_cube:
        return _wrap_cube(pos, board)
    else:
        return _wrap_2d(pos, board)


def _step(pos, board, is_cube=False):
    x, y, facing = pos
    potential_new_positions = {
        FACING[RIGHT]: (x + 1, y),
        FACING[LEFT]: (x - 1, y),
        FACING[DOWN]: (x, y + 1),
        FACING[UP]: (x, y - 1),
    }
    x, y = potential_new_positions[facing]
    if (x, y) not in board:
        x, y, facing = _wrap(pos, board, is_cube)
    if (x, y) not in board:
        import pdb

        pdb.set_trace()
    if board[x, y] == SOLID_WALL:
        return pos
    else:
        return Position(x=x, y=y, facing=facing)


def final_password(puzzle_input, is_cube=False):
    board, path = _parse_input(puzzle_input)
    pos = Position(
        x=min(x for x, y in board if board[x, y] == OPEN_TILE and y == STARTING_Y),
        y=STARTING_Y,
        facing=FACING[RIGHT],
    )

    for step in path:
        if isinstance(step, int):
            for _ in range(step):
                pos = _step(pos, board, is_cube=is_cube)
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
    print(f"Part 2: {final_password(puzzle_input, is_cube=True)}")
