import numpy as np

from util import read_puzzle_input

ROOM_WIDTH = 7

HORIZONTAL_LINE = ((0, 0), (1, 0), (2, 0), (3, 0))
PLUS = ((1, 0), (0, 1), (1, 1), (2, 1), (2, 2))
L = ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2))
VERTICAL_LINE = ((0, 0), (0, 1), (0, 2), (0, 3))
BOX = ((0, 0), (1, 0), (0, 1), (1, 1))

SHAPE_ORDER = (HORIZONTAL_LINE, PLUS, L, VERTICAL_LINE, BOX)

RIGHT = ">"


def _jet_stream_move_invalid(next_coords, room):
    if any(x >= ROOM_WIDTH or x < 0 for x, _ in next_coords):
        return True

    for room_coord in room:
        for coord in next_coords:
            if np.array_equal(room_coord, coord):
                return True
    return False


def _move_down_invalid(next_coords, room):
    if any(y < 0 for _, y in next_coords):
        return True

    for room_coord in room:
        for coord in next_coords:
            if np.array_equal(room_coord, coord):
                return True

    return False


def rock_tower_height(puzzle_input, rock_limit=2022):
    jet_pattern = puzzle_input.strip()
    room = []
    num_rocks_fallen = 0
    jet_pushes = 0
    while num_rocks_fallen < rock_limit:
        next_rock = SHAPE_ORDER[num_rocks_fallen % len(SHAPE_ORDER)]
        rock_height = max(y for _, y in room) + 3 if num_rocks_fallen > 0 else 3
        rock_coords = [
            np.array((2, rock_height)) + np.array(coord) for coord in next_rock
        ]

        while True:
            # Get pushed by the gas jet
            direction = jet_pattern[jet_pushes % len(jet_pattern)]
            push = np.array((1, 0)) if direction == RIGHT else np.array((-1, 0))
            next_coords = [push + coord for coord in rock_coords]
            if _jet_stream_move_invalid(next_coords, room):
                # Invalid move
                pass
            else:
                rock_coords = next_coords

            jet_pushes += 1

            # Move down
            next_coords = [np.array((0, -1)) + coord for coord in rock_coords]
            if _move_down_invalid(next_coords, room):
                # Invalid move
                break
            rock_coords = next_coords
        room += rock_coords
        num_rocks_fallen += 1
    return 0


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {rock_tower_height(puzzle_input)}")
    print(f"Part 2: {rock_tower_height(puzzle_input)}")
