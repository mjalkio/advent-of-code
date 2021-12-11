from collections import defaultdict

from util import read_puzzle_input

# See: http://devmag.org.za/2013/08/31/geometry-with-hex-coordinates/
# ...except there are typos, but it has the right idea
DIRECTION_VECTORS = {
    "e": (1, 0, -1),
    "ne": (0, 1, -1),
    "nw": (-1, 1, 0),
    "w": (-1, 0, 1),
    "sw": (0, -1, 1),
    "se": (1, -1, 0),
}


def _add_coordinates(a, b):
    return tuple(coord_a + coord_b for coord_a, coord_b in zip(a, b))


def _get_tile_coordinates(directions, reference_tile=(0, 0, 0)):
    """"""
    tile_coordinates = reference_tile
    i = 0
    while i < len(directions):
        if directions[i] in ("n", "s"):
            next_direction = directions[i : i + 2]
            i += 2
        else:
            next_direction = directions[i]
            i += 1

        next_direction_vector = DIRECTION_VECTORS[next_direction]
        tile_coordinates = _add_coordinates(tile_coordinates, next_direction_vector)
    return tile_coordinates


def _get_black_tiles(puzzle_input):
    tile_directions = [line for line in puzzle_input.split("\n") if line != ""]
    black_tiles = set()
    for directions in tile_directions:
        tile_coordinates = _get_tile_coordinates(directions)
        if tile_coordinates in black_tiles:
            black_tiles.remove(tile_coordinates)
        else:
            black_tiles.add(tile_coordinates)
    return black_tiles


def get_num_black_tiles(puzzle_input):
    black_tiles = _get_black_tiles(puzzle_input)
    return len(black_tiles)


def get_num_black_tiles_after_days(puzzle_input, num_days):
    black_tiles = _get_black_tiles(puzzle_input)
    for _ in range(num_days):
        black_neighbor_counts = defaultdict(int)

        for bt in black_tiles:
            neighbor_coordinates = [
                _add_coordinates(bt, direction)
                for direction in DIRECTION_VECTORS.values()
            ]
            for neighbor in neighbor_coordinates:
                black_neighbor_counts[neighbor] += 1

        new_black_tiles = set()
        for tile, num_black_tiles in black_neighbor_counts.items():
            if tile in black_tiles and num_black_tiles in (1, 2):
                new_black_tiles.add(tile)
            elif tile not in black_tiles and num_black_tiles == 2:
                new_black_tiles.add(tile)
        black_tiles = new_black_tiles
    return len(black_tiles)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_num_black_tiles(puzzle_input)}")
    print(
        f"Part 2: {get_num_black_tiles_after_days(puzzle_input=puzzle_input, num_days=100)}"
    )
