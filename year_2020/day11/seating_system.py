from util import read_puzzle_input

EMPTY_SEAT = 'L'
FLOOR = '.'
OCCUPIED_SEAT = '#'


def _get_seat_layout(puzzle_input):
    lines = [line for line in puzzle_input.split('\n') if line != '']
    seat_layout = {}
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            seat_layout[(i, j)] = lines[i][j]
    return seat_layout


def _get_num_occupied_seats(seat_layout):
    return sum(seat == OCCUPIED_SEAT for seat in seat_layout.values())


def get_num_occupied_seats_at_convergence(puzzle_input):
    seat_layout = _get_seat_layout(puzzle_input)
    return _get_num_occupied_seats(seat_layout)


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_num_occupied_seats_at_convergence(puzzle_input)}")
    print(f"Part 2: {None}")
