import math

from util import read_puzzle_input

UPPER = 1
LOWER = 2


def _binary_partition(partitioning, num_seats):
    if 2 ** len(partitioning) != num_seats:
        raise ValueError("Invalid input for binary partitioning!")

    seats = range(num_seats)
    for step in partitioning:
        # import pdb; pdb.set_trace()
        if step == UPPER:
            seats = seats[len(seats) // 2 :]
        elif step == LOWER:
            seats = seats[: len(seats) // 2]
        else:
            raise ValueError("Invalid character found in _binary_partition")

    assert len(seats) == 1
    return seats[0]


def seat_row(row_space_partitioning, num_rows=128):
    return _binary_partition(
        partitioning=[
            UPPER if char == "B" else LOWER for char in row_space_partitioning
        ],
        num_seats=num_rows,
    )


def seat_column(column_space_partitioning, num_columns=8):
    return _binary_partition(
        partitioning=[
            UPPER if char == "R" else LOWER for char in column_space_partitioning
        ],
        num_seats=num_columns,
    )


def seat_id(space_partitioning, num_rows=128, num_columns=8):
    num_chars_row_space_partitioning = int(math.log(num_rows, 2))
    num_chars_column_space_partitioning = int(math.log(num_columns, 2))
    expected_num_chars_space_partitioning = (
        num_chars_row_space_partitioning + num_chars_column_space_partitioning
    )
    assert expected_num_chars_space_partitioning == len(space_partitioning)

    row = seat_row(
        row_space_partitioning=space_partitioning[:num_chars_row_space_partitioning],
        num_rows=num_rows,
    )
    column = seat_column(
        column_space_partitioning=space_partitioning[num_chars_row_space_partitioning:],
        num_columns=num_columns,
    )
    return row * 8 + column


def highest_seat_id(puzzle_input):
    space_partitionings = puzzle_input.split("\n")
    return max(seat_id(space_partitioning=sp) for sp in space_partitionings)


def my_seat(puzzle_input):
    space_partitionings = puzzle_input.split("\n")
    taken_seats = [seat_id(space_partitioning=sp) for sp in space_partitionings]
    taken_seats.sort()
    for i in range(len(taken_seats)):
        if taken_seats[i] == taken_seats[i + 1] - 2:
            return taken_seats[i] + 1


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {highest_seat_id(puzzle_input)}")
    print(f"Part 2: {my_seat(puzzle_input)}")
