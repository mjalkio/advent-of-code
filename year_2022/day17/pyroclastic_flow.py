from collections import namedtuple

from util import read_puzzle_input

ROOM_WIDTH = 7

HORIZONTAL_LINE = ((0, 1), (1, 1), (2, 1), (3, 1))
PLUS = ((1, 1), (0, 2), (1, 2), (2, 2), (1, 3))
L = ((0, 1), (1, 1), (2, 1), (2, 2), (2, 3))
VERTICAL_LINE = ((0, 1), (0, 2), (0, 3), (0, 4))
BOX = ((0, 1), (1, 1), (0, 2), (1, 2))

SHAPE_ORDER = (HORIZONTAL_LINE, PLUS, L, VERTICAL_LINE, BOX)

RIGHT = ">"

PRINT_BUFFER = 7

CacheKey = namedtuple("CacheKey", ["top_blocks", "block_type", "wind_direction"])
CACHE_HEIGHT = 20


def _jet_stream_move_invalid(next_coords, room):
    return any(
        coord[0] >= ROOM_WIDTH or coord[0] < 0 or coord in room for coord in next_coords
    )


def _move_down_invalid(next_coords, room):
    return any(coord[1] < 0 or coord in room for coord in next_coords)


def _add(point_a, point_b):
    return (point_a[0] + point_b[0], point_a[1] + point_b[1])


def _print_room(room, rock_coords):
    str_room = "\n\n"
    if len(room) == 0:
        max_y = PRINT_BUFFER
    else:
        max_y = max(y for _, y in room) + PRINT_BUFFER
    for y in reversed(range(max_y + 1)):
        str_room += "|"
        for x in range(ROOM_WIDTH):
            if (x, y) in room:
                str_room += "#"
            elif (x, y) in rock_coords:
                str_room += "@"
            else:
                str_room += "."
        str_room += "|\n"
    str_room += "+-------+"
    print(str_room)


def rock_tower_height(puzzle_input, rock_limit=2022):
    cache = {}
    tower_height_addition = None

    jet_pattern = puzzle_input.strip()
    room = set()
    num_rocks_fallen = 0
    jet_pushes = 0
    tower_height = 0
    while num_rocks_fallen < rock_limit:
        next_rock = SHAPE_ORDER[num_rocks_fallen % len(SHAPE_ORDER)]
        new_rock_y = tower_height + 2
        rock_coords = [_add((2, new_rock_y), coord) for coord in next_rock]

        top_blocks = []
        for y in range(tower_height - CACHE_HEIGHT, tower_height):
            layer = []
            for x in range(ROOM_WIDTH):
                if (x, y) in room:
                    layer.append(1)
                else:
                    layer.append(0)
            top_blocks.append(tuple(layer))
        top_blocks = tuple(top_blocks)

        key = CacheKey(
            top_blocks=top_blocks,
            block_type=next_rock,
            wind_direction=jet_pattern[jet_pushes % len(jet_pattern)],
        )

        if cache is not None and key in cache:
            cached_rocks_fallen, cached_tower_height = cache[key]
            loop_size = num_rocks_fallen - cached_rocks_fallen
            num_loops_to_limit = (rock_limit - num_rocks_fallen) // loop_size
            num_rocks_fallen += num_loops_to_limit * loop_size

            tower_height_addition = num_loops_to_limit * (
                tower_height - cached_tower_height
            )

            cache = None  # Remove the cache so we can finish "normally"
        elif cache is not None and num_rocks_fallen > 3_000:
            cache[key] = num_rocks_fallen, tower_height

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
        tower_height = max(tower_height, max(y for _, y in rock_coords) + 1)
        num_rocks_fallen += 1
    if tower_height_addition is not None:
        return tower_height + tower_height_addition
    return tower_height


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {rock_tower_height(puzzle_input)}")
    print(f"Part 2: {rock_tower_height(puzzle_input, rock_limit=1_000_000_000_000)}")
