import math

from util import read_puzzle_input

SAND_SOURCE = (500, 0)


def _print_map(sand_map):
    min_x = math.inf
    min_y = math.inf
    max_x = 0
    max_y = 0
    for x, y in sand_map.keys():
        min_x = min(x, min_x)
        min_y = min(y, min_y)
        max_x = max(x, max_x)
        max_y = max(y, max_y)

    for y in range(min_y, max_y + 1):
        line = ""
        for x in range(min_x, max_x + 1):
            if (x, y) in sand_map:
                line += sand_map[x, y]
            else:
                line += "."
        print(line)


def num_resting_units(puzzle_input):
    sand_map = {SAND_SOURCE: "+"}

    lines = puzzle_input.split("\n")
    for line in lines:
        points = line.split(" -> ")
        for i in range(len(points) - 1):
            x1, y1 = [int(num) for num in points[i].split(",")]
            x2, y2 = [int(num) for num in points[i + 1].split(",")]

            if x1 == x2:
                # Vertical line
                min_y = min(y1, y2)
                max_y = max(y1, y2)
                for y in range(min_y, max_y + 1):
                    sand_map[x1, y] = "#"
            elif y1 == y2:
                min_x = min(x1, x2)
                max_x = max(x1, x2)
                for x in range(min_x, max_x + 1):
                    sand_map[x, y1] = "#"
            else:
                raise ValueError("Uh oh!")

    lowest_rock_y = max(y for _, y in sand_map.keys())

    sand_x, sand_y = SAND_SOURCE
    while sand_y <= lowest_rock_y:
        if (sand_x, sand_y + 1) not in sand_map:
            sand_y += 1
        elif (sand_x - 1, sand_y + 1) not in sand_map:
            sand_x -= 1
            sand_y += 1
        elif (sand_x + 1, sand_y + 1) not in sand_map:
            sand_x += 1
            sand_y += 1
        else:
            sand_map[sand_x, sand_y] = "o"
            sand_x, sand_y = SAND_SOURCE

    # If the sand drops below the lowest rock, it will fall forever
    return sum(obj == "o" for obj in sand_map.values())


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {num_resting_units(puzzle_input)}")
    print(f"Part 2: {num_resting_units(puzzle_input)}")
