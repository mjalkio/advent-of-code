from util import read_puzzle_input


def num_visible_trees(puzzle_input):
    lines = [line for line in puzzle_input.split("\n") if line != ""]
    num_rows = len(lines)
    num_cols = len(lines[0])

    tree_height_map = {}
    for i in range(num_rows):
        for j in range(num_cols):
            tree_height_map[(i, j)] = int(lines[i][j])
    return 0


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {num_visible_trees(puzzle_input)}")
    print(f"Part 2: {num_visible_trees(puzzle_input)}")
