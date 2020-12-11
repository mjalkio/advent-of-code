from collections import defaultdict

from util import read_puzzle_input

EMPTY_SEAT = 'L'
FLOOR = '.'
OCCUPIED_SEAT = '#'


def _get_seat_layout(puzzle_input):
    lines = [line for line in puzzle_input.split('\n') if line != '']
    seat_layout = {}
    for j in range(len(lines)):
        for i in range(len(lines[j])):
            seat_layout[(i, j)] = lines[j][i]
    return seat_layout


def _get_num_occupied_seats(seat_layout):
    return sum(seat == OCCUPIED_SEAT for seat in seat_layout.values())


def _get_surrounding_chairs(seat_layout):
    surrounding_chairs = defaultdict(list)
    for (i, j) in seat_layout.keys():
        for ii in range(i - 1, i + 2):
            for jj in range(j - 1, j + 2):
                if ii == i and jj == j:
                    continue

                if seat_layout.get((ii, jj)) in (EMPTY_SEAT, OCCUPIED_SEAT):
                    surrounding_chairs[(i, j)].append((ii, jj))
    return surrounding_chairs


def get_surrounding_chairs_part_2(seat_layout):
    surrounding_chairs = defaultdict(list)
    directions = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                directions.append((i, j))

    for (x, y) in seat_layout.keys():
        for dx, dy in directions:
            possible_surrounding_x = x + dx
            possible_surrounding_y = y + dy
            while seat_layout.get((possible_surrounding_x, possible_surrounding_y)) == FLOOR:
                possible_surrounding_x += dx
                possible_surrounding_y += dy
            if seat_layout.get((possible_surrounding_x, possible_surrounding_y)) in (
                EMPTY_SEAT, OCCUPIED_SEAT
            ):
                surrounding_chairs[(x, y)].append((possible_surrounding_x, possible_surrounding_y))
    return surrounding_chairs


def _get_num_occupied_seats_around(i, j, seat_layout, surrounding_chairs):
    return sum(seat_layout[(ii, jj)] == OCCUPIED_SEAT for ii, jj in surrounding_chairs[(i, j)])


def _get_next_seat_layout(seat_layout, surrounding_chairs, max_surrounding_occupied=4):
    next_seat_layout = {}
    for (i, j), current_state in seat_layout.items():
        if (
            current_state == EMPTY_SEAT
            and _get_num_occupied_seats_around(i, j, seat_layout, surrounding_chairs) == 0
        ):
            next_seat_layout[(i, j)] = OCCUPIED_SEAT
        elif (
            current_state == OCCUPIED_SEAT
            and (
                _get_num_occupied_seats_around(i, j, seat_layout, surrounding_chairs)
                >= max_surrounding_occupied
            )
        ):
            next_seat_layout[(i, j)] = EMPTY_SEAT
        else:
            next_seat_layout[(i, j)] = current_state

    return next_seat_layout


def _are_layouts_the_same(seat_layout_1, seat_layout_2):
    if len(seat_layout_1) != len(seat_layout_2):
        raise ValueError('Seat layouts being compared have different numbers of seats!')
    for i, j in seat_layout_1:
        if seat_layout_1[(i, j)] != seat_layout_2[(i, j)]:
            return False
    return True


def print_layout(seat_layout):
    width = max(x for x, y in seat_layout.keys()) + 1
    height = max(y for x, y in seat_layout.keys()) + 1
    for j in range(height):
        line = []
        for i in range(width):
            line.append(seat_layout[(i, j)])
        print(''.join(line))


def get_num_occupied_seats_at_convergence(
    puzzle_input,
    surrounding_chair_fn=_get_surrounding_chairs,
    max_surrounding_occupied=4,
):
    seat_layout = _get_seat_layout(puzzle_input)
    surrounding_chairs = surrounding_chair_fn(seat_layout)
    next_seat_layout = _get_next_seat_layout(
        seat_layout=seat_layout,
        surrounding_chairs=surrounding_chairs,
        max_surrounding_occupied=max_surrounding_occupied,
    )
    while not _are_layouts_the_same(seat_layout, next_seat_layout):
        seat_layout = next_seat_layout
        next_seat_layout = _get_next_seat_layout(
            seat_layout=seat_layout,
            surrounding_chairs=surrounding_chairs,
            max_surrounding_occupied=max_surrounding_occupied,
        )
    return _get_num_occupied_seats(seat_layout)


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_num_occupied_seats_at_convergence(puzzle_input)}")
    part_2_answer = get_num_occupied_seats_at_convergence(
        puzzle_input=puzzle_input,
        surrounding_chair_fn=get_surrounding_chairs_part_2,
        max_surrounding_occupied=5,
    )
    print(f"Part 2: {part_2_answer}")
