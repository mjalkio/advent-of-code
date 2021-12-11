from util import read_puzzle_input


def get_low_point_risk_level_sum(puzzle_input):
    lines = puzzle_input.split("\n")
    risk_level = 0
    heightmap = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            heightmap[(x, y)] = int(lines[y][x])

    for (x, y), height in heightmap.items():
        adjacent = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        if all(
            heightmap[(xx, yy)] > height for xx, yy in adjacent if (xx, yy) in heightmap
        ):
            risk_level += height + 1

    return risk_level


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_low_point_risk_level_sum(puzzle_input)}")
    print(f"Part 2: {get_low_point_risk_level_sum(puzzle_input)}")
