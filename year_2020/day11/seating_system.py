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


def _get_num_occupied_seats_around(i, j, seat_layout):
    num_occupied_seats_around = 0
    for ii in range(i - 1, i + 2):
        for jj in range(j - 1, j + 2):
            if ii == 0 and jj == 0:
                continue

            if seat_layout.get((i, j)) == OCCUPIED_SEAT:
                num_occupied_seats_around += 1
    return num_occupied_seats_around


def _get_next_seat_layout(seat_layout):
    next_seat_layout = {}
    for (i, j), current_state in seat_layout.items():
        if (
            current_state == EMPTY_SEAT
            and _get_num_occupied_seats_around(i, j, seat_layout) == 0
        ):
            next_seat_layout[(i, j)] = OCCUPIED_SEAT
        elif (
            current_state == OCCUPIED_SEAT
            and _get_num_occupied_seats_around(i, j, seat_layout) >= 4
        ):
            next_seat_layout[(i, j)] = EMPTY_SEAT
        else:
            next_seat_layout[(i, j)] = current_state

    return next_seat_layout


def get_num_occupied_seats_at_convergence(puzzle_input):
    seat_layout = _get_seat_layout(puzzle_input)
    next_seat_layout = _get_next_seat_layout(seat_layout)
    while seat_layout != next_seat_layout:
        seat_layout = next_seat_layout
        next_seat_layout = _get_next_seat_layout(seat_layout)
    return _get_num_occupied_seats(seat_layout)


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_num_occupied_seats_at_convergence(puzzle_input)}")
    print(f"Part 2: {None}")
