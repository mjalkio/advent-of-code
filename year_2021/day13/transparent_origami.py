from util import read_puzzle_input


def get_dot_map(puzzle_input, num_folds=None):
    dot_lines, fold_lines = [line.split("\n") for line in puzzle_input.split("\n\n")]
    dot_map = set()
    for line in dot_lines:
        x, y = [int(coord) for coord in line.split(",")]
        dot_map.add((x, y))

    num_folds = num_folds if num_folds is not None else len(fold_lines)
    for line in fold_lines[:num_folds]:
        instruction, line_num = line.split("=")
        if instruction == "fold along x":
            fold_idx = 0
        else:
            fold_idx = 1

        line_num = int(line_num)
        new_dot_map = set()
        for coord in dot_map:
            if coord[fold_idx] < line_num:
                new_dot_map.add(coord)
                continue
            distance_from_fold = coord[fold_idx] - line_num
            mutable_coord = list(coord)
            mutable_coord[fold_idx] = line_num - distance_from_fold
            new_dot_map.add(tuple(mutable_coord))
        dot_map = new_dot_map
    return dot_map


def get_num_dots(puzzle_input, num_folds=1):
    return len(get_dot_map(puzzle_input=puzzle_input, num_folds=num_folds))


def print_map(dot_map):
    width = max(x for x, _ in dot_map) + 1
    height = max(y for _, y in dot_map) + 1
    for y in range(height):
        line = []
        for x in range(width):
            line.append("#" if (x, y) in dot_map else ".")
        print("".join(line))


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_num_dots(puzzle_input)}")
    print("Part 2:")
    print_map(get_dot_map(puzzle_input))
