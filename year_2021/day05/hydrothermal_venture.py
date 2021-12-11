from collections import defaultdict

from util import read_puzzle_input


def get_num_dangerous_points(puzzle_input, use_diagonal_lines=False):
    lines = puzzle_input.split("\n")

    line_counts = defaultdict(int)
    for line in lines:
        start_pt, end_pt = line.split(" -> ")
        x1, y1 = [int(coord) for coord in start_pt.split(",")]
        x2, y2 = [int(coord) for coord in end_pt.split(",")]

        if x1 == x2:
            start_y, end_y = sorted([y1, y2])
            for y in range(start_y, end_y + 1):
                line_counts[(x1, y)] += 1
        elif y1 == y2:
            start_x, end_x = sorted([x1, x2])
            for x in range(start_x, end_x + 1):
                line_counts[(x, y1)] += 1
        elif use_diagonal_lines:
            x_dir = -1 if x1 > x2 else 1
            y_dir = -1 if y1 > y2 else 1
            length = abs(x1 - x2)
            for i in range(length + 1):
                line_counts[(x1 + x_dir * i, y1 + y_dir * i)] += 1

    return sum([count >= 2 for count in line_counts.values()])


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_num_dangerous_points(puzzle_input)}")
    print(f"Part 2: {get_num_dangerous_points(puzzle_input, use_diagonal_lines=True)}")
