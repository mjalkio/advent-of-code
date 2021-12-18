from util import read_puzzle_input


MAX_Y_VEL = 200  # Random large value to restrict the search space


def get_highest_possible_y_position(puzzle_input):
    puzzle_input_left, y_str = puzzle_input.split(", y=")
    _, x_str = puzzle_input_left.split(" x=")
    x_range = [int(pos) for pos in x_str.split("..")]
    y_range = [int(pos) for pos in y_str.split("..")]

    highest_possible_y_pos = 0
    for test_y_vel in reversed(range(MAX_Y_VEL)):
        for x_vel in range(x_range[0] + 1):
            x = 0
            y = 0
            max_y = 0
            y_vel = test_y_vel
            while x <= x_range[1] and y_range[0] <= y:
                if x_range[0] <= x <= x_range[1] and y_range[0] <= y <= y_range[1]:
                    highest_possible_y_pos = max(highest_possible_y_pos, max_y)
                x += x_vel
                y += y_vel
                if x_vel > 0:
                    x_vel -= 1
                y_vel -= 1

                max_y = max(max_y, y)

    return highest_possible_y_pos


def get_num_valid_initial_velocities(puzzle_input):
    return 0


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_highest_possible_y_position(puzzle_input)}")
    print(f"Part 2: {get_num_valid_initial_velocities(puzzle_input)}")
