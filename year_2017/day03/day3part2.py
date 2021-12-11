def new_spiral_value(x, y, spiral):
    surrounding = (
        (x + 1, y),
        (x + 1, y + 1),
        (x, y + 1),
        (x - 1, y + 1),
        (x - 1, y),
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
    )

    return sum([spiral.get(coord, 0) for coord in surrounding])


def first_spiral_value_larger(num):
    spiral = {(0, 0): 1}

    x = 1
    y = 1
    side_length = 1

    while True:
        side_length += 2

        while y < int(side_length / 2):
            y += 1
            spiral[(x, y)] = new_spiral_value(x, y, spiral)
        while x > -1 * int(side_length / 2):
            x -= 1
            spiral[(x, y)] = new_spiral_value(x, y, spiral)
        while y > -1 * int(side_length / 2):
            y -= 1
            spiral[(x, y)] = new_spiral_value(x, y, spiral)
        while x < int(side_length / 2):
            x += 1
            spiral[(x, y)] = new_spiral_value(x, y, spiral)

        current_values = list(spiral.values())
        current_values.sort()
        for val in current_values:
            if val > num:
                return val


if __name__ == "__main__":
    puzzle_input = 361527
    print(first_spiral_value_larger(puzzle_input))
