def data_coordinates(loc):
    spiral_level = 0
    side_length = 1

    max_data_value_in_level = 1
    while loc > max_data_value_in_level:
        spiral_level += 1
        side_length = side_length + 2
        max_data_value_in_level += side_length * 4 - 4

    x = spiral_level
    y = -spiral_level
    data_val_at_x_y = max_data_value_in_level
    if data_val_at_x_y == loc:
        return (x, y)

    for side in range(4):
        for _ in range(side_length - 1):
            if data_val_at_x_y == loc:
                return (x, y)

            if side == 0:
                x -= 1
            elif side == 1:
                y += 1
            elif side == 2:
                x += 1
            elif side == 3:
                y -= 1

            data_val_at_x_y -= 1

    raise Exception("That didn't work...")


def manhattan_distance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])


def spiral_manhattan_distance(loc):
    coords = data_coordinates(loc)
    return manhattan_distance(coords, (0, 0))

if __name__ == '__main__':
    puzzle_input = 361527
    print(spiral_manhattan_distance(puzzle_input))
