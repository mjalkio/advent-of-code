from util import read_puzzle_input

FORWARD = 'F'
LEFT = 'L'
RIGHT = 'R'
NORTH = 'N'
EAST = 'E'
SOUTH = 'S'
WEST = 'W'
DIRECTIONS = (NORTH, EAST, SOUTH, WEST)


def get_navigation_destination(puzzle_input, x=0, y=0, initial_direction=EAST):
    instructions = [line for line in puzzle_input.split('\n') if line != '']
    current_direction_idx = DIRECTIONS.index(initial_direction)
    for instruction in instructions:
        action = instruction[0]
        value = int(instruction[1:])
        if action in (LEFT, RIGHT):
            turn = (-1 if action == LEFT else 1) * value // 90
            current_direction_idx = (current_direction_idx + turn) % len(DIRECTIONS)
            continue
        if action == FORWARD:
            action = DIRECTIONS[current_direction_idx]

        if action == NORTH:
            y += value
        elif action == SOUTH:
            y -= value
        elif action == EAST:
            x += value
        elif action == WEST:
            x -= value

    return x, y


def get_navigation_destination_with_waypoint(
    puzzle_input,
    x=0,
    y=0,
    initial_direction=EAST,
    waypoint_x=10,
    waypoint_y=1,
):
    instructions = [(line[0], int(line[1:])) for line in puzzle_input.split('\n') if line != '']
    for action, value in instructions:
        if action in (RIGHT, LEFT):
            num_rotations = value // 90
            for i in range(num_rotations):
                waypoint_x, waypoint_y = (
                    (-1 if action == LEFT else 1) * waypoint_y,
                    (-1 if action == RIGHT else 1) * waypoint_x
                )
        elif action == NORTH:
            waypoint_y += value
        elif action == SOUTH:
            waypoint_y -= value
        elif action == EAST:
            waypoint_x += value
        elif action == WEST:
            waypoint_x -= value
        elif action == FORWARD:
            x += (waypoint_x * value)
            y += (waypoint_y * value)

    return x, y


def get_manhattan_distance_after_navigation(
    puzzle_input,
    starting_x=0,
    starting_y=0,
    use_waypoint=False,
):
    if use_waypoint:
        ending_x, ending_y = get_navigation_destination_with_waypoint(puzzle_input=puzzle_input)
    else:
        ending_x, ending_y = get_navigation_destination(puzzle_input=puzzle_input,)
    return abs(ending_x - starting_x) + abs(ending_y - starting_y)


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_manhattan_distance_after_navigation(puzzle_input)}")
    print(f"Part 2: {get_manhattan_distance_after_navigation(puzzle_input, use_waypoint=True)}")
