from math import prod

import numpy as np

from util import read_puzzle_input


def _parse_tiles(puzzle_input):
    """Take the input, return a map of ID to tile."""
    tiles = {}
    tile_definitions = puzzle_input.split('\n\n')
    for tile_def in tile_definitions:
        tile_lines = tile_def.split('\n')
        tile_id = int(tile_lines[0][5:-1])
        tiles[tile_id] = np.array([list(tile_line) for tile_line in tile_lines[1:]])
    return tiles


def _get_tile_potential_borders(tile):
    tile_sides = [tile[0], tile[-1], tile[:, 0], tile[:, -1]]
    # With the magic of rotation and such, we can make any border reversed as well
    potential_borders = set()
    for side in tile_sides:
        potential_borders.add(''.join(side))
        potential_borders.add(''.join(reversed(side)))
    return potential_borders


def _shares_border(tile_a, tile_b):
    tile_a_potential_borders = _get_tile_potential_borders(tile_a)
    tile_b_potential_borders = _get_tile_potential_borders(tile_b)
    return len(tile_a_potential_borders.intersection(tile_b_potential_borders)) > 0


def _get_potential_neighbors(tiles):
    """Return a map of tile IDs to the IDs of potential neighbors."""
    potential_neighbors = {}
    for tile_id in tiles:
        potential_neighbors[tile_id] = set(
            neighbor_id
            for neighbor_id
            in tiles
            if neighbor_id != tile_id and _shares_border(tiles[tile_id], tiles[neighbor_id])
        )
    return potential_neighbors


def get_corner_ids_product(puzzle_input):
    tiles = _parse_tiles(puzzle_input)
    potential_neighbors = _get_potential_neighbors(tiles)

    # If a tile only has two neighbors, it MUST be a corner tile.
    # The "potential" neighbors are definitely its neighbors.
    corner_tile_ids = [
        tile_id
        for tile_id
        in potential_neighbors
        if len(potential_neighbors[tile_id]) == 2
    ]
    if len(corner_tile_ids) > 4:
        raise ValueError('Have not implemented for this situation...')
    return prod(corner_tile_ids)


def get_water_roughness(puzzle_input):
    return None


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_corner_ids_product(puzzle_input)}")
    print(f"Part 2: {None}")
