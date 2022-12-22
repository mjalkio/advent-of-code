from util import read_puzzle_input

RIGHT = "R"
LEFT = "L"


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
    return 0


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {final_password(puzzle_input)}")
    print(f"Part 2: {final_password(puzzle_input)}")
