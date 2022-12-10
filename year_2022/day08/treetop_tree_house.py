from util import read_puzzle_input


def num_visible_trees(puzzle_input):
    lines = [line for line in puzzle_input.split("\n") if line != ""]
    num_rows = len(lines)
    num_cols = len(lines[0])

    tree_height_map = {}
    for i in range(num_rows):
        for j in range(num_cols):
            tree_height_map[i, j] = int(lines[i][j])

    num_visible = 0
    for i, j in tree_height_map:
        if (
            all(tree_height_map[ii, j] < tree_height_map[i, j] for ii in range(0, i))
            or all(
                tree_height_map[ii, j] < tree_height_map[i, j]
                for ii in range(i + 1, num_rows)
            )
            or all(tree_height_map[i, jj] < tree_height_map[i, j] for jj in range(0, j))
            or all(
                tree_height_map[i, jj] < tree_height_map[i, j]
                for jj in range(j + 1, num_cols)
            )
        ):
            num_visible += 1

    return num_visible


def highest_scenic_score(puzzle_input):
    return 0


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {num_visible_trees(puzzle_input)}")
    print(f"Part 2: {num_visible_trees(puzzle_input)}")
