from util import read_puzzle_input


def get_num_dots(puzzle_input):
    dot_lines, fold_lines = [line.split("\n") for line in puzzle_input.split("\n\n")]
    dot_map = set()
    for line in dot_lines:
        x, y = [int(coord) for coord in line.split(",")]
        dot_map.add((x, y))

    instruction, line_num = fold_lines[0].split("=")
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
    return len(new_dot_map)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_num_dots(puzzle_input)}")
    print(f"Part 2: {get_num_dots(puzzle_input)}")
