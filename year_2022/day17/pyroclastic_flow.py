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
    return any(
        coord[0] >= ROOM_WIDTH or coord[0] < 0 or coord in room for coord in next_coords
    )


def _move_down_invalid(next_coords, room):
    return any(coord[1] < 0 or coord in room for coord in next_coords)


def _add(point_a, point_b):
    return (point_a[0] + point_b[0], point_a[1] + point_b[1])


def rock_tower_height(puzzle_input, rock_limit=2022):
    jet_pattern = puzzle_input.strip()
    room = set()
    num_rocks_fallen = 0
    jet_pushes = 0
    while num_rocks_fallen < rock_limit:
        next_rock = SHAPE_ORDER[num_rocks_fallen % len(SHAPE_ORDER)]
        rock_height = max(y for _, y in room) + 3 if num_rocks_fallen > 0 else 3
        rock_coords = [_add((2, rock_height), coord) for coord in next_rock]

        while True:
            # Get pushed by the gas jet
            direction = jet_pattern[jet_pushes % len(jet_pattern)]
            push = (1, 0) if direction == RIGHT else (-1, 0)
            next_coords = [_add(push, coord) for coord in rock_coords]
            if _jet_stream_move_invalid(next_coords, room):
                # Invalid move
                pass
            else:
                rock_coords = next_coords

            jet_pushes += 1

            # Move down
            next_coords = [_add((0, -1), coord) for coord in rock_coords]
            if _move_down_invalid(next_coords, room):
                # Invalid move
                break
            rock_coords = next_coords
        room.update(rock_coords)
        num_rocks_fallen += 1
    return max(y for _, y in room)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {rock_tower_height(puzzle_input)}")
    print(f"Part 2: {rock_tower_height(puzzle_input)}")
