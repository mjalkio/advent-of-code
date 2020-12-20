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


def get_corner_ids_product(puzzle_input):
    tiles = _parse_tiles(puzzle_input)
    return None


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_corner_ids_product(puzzle_input)}")
    print(f"Part 2: {None}")
