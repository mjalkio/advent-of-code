import math

import numpy as np

from util import read_puzzle_input

SEA_MONSTER_LENGTH = 20
SEA_MONSTER_HEIGHT = 3


def _parse_tiles(puzzle_input):
    """Take the input, return a map of ID to tile."""
    tiles = {}
    tile_definitions = puzzle_input.split("\n\n")
    for tile_def in tile_definitions:
        tile_lines = tile_def.split("\n")
        tile_id = int(tile_lines[0][5:-1])
        tiles[tile_id] = np.array([list(tile_line) for tile_line in tile_lines[1:]])
    return tiles


def _get_tile_potential_borders(tile):
    tile_sides = [tile[0], tile[-1], tile[:, 0], tile[:, -1]]
    # With the magic of rotation and such, we can make any border reversed as well
    potential_borders = set()
    for side in tile_sides:
        potential_borders.add("".join(side))
        potential_borders.add("".join(reversed(side)))
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
            for neighbor_id in tiles
            if neighbor_id != tile_id
            and _shares_border(tiles[tile_id], tiles[neighbor_id])
        )
    return potential_neighbors


def _get_corner_tile_ids(potential_neighbors):
    return [
        tile_id
        for tile_id in potential_neighbors
        if len(potential_neighbors[tile_id]) == 2
    ]


def get_corner_ids_product(puzzle_input):
    tiles = _parse_tiles(puzzle_input)
    potential_neighbors = _get_potential_neighbors(tiles)

    # If a tile only has two neighbors, it MUST be a corner tile.
    # The "potential" neighbors are definitely its neighbors.
    corner_tile_ids = _get_corner_tile_ids(potential_neighbors)
    if len(corner_tile_ids) > 4:
        raise ValueError("Have not implemented for this situation...")
    return math.prod(corner_tile_ids)


def _has_border(tile, border):
    reversed_border = border[::-1]
    tile_sides = [tile[0], tile[-1], tile[:, 0], tile[:, -1]]
    return any(
        np.array_equal(border, s) or np.array_equal(reversed_border, s)
        for s in tile_sides
    )


def _match_left_right(left_tile, right_tile):
    return np.array_equal(left_tile[:, -1], right_tile[:, 0])


def _match_top_bottom(top_tile, bottom_tile):
    return np.array_equal(top_tile[-1], bottom_tile[0])


def _find_fit(tile, left_tile_info, top_tile_info):
    # A tile can be rotated/flipped into eight positions. Try them all.
    tile_possibilities = [
        tile,
        np.rot90(tile),
        np.rot90(np.rot90(tile)),
        np.rot90(np.rot90(np.rot90(tile))),
        np.fliplr(tile),
        np.rot90(np.fliplr(tile)),
        np.rot90(np.rot90(np.fliplr(tile))),
        np.rot90(np.rot90(np.rot90(np.fliplr(tile)))),
    ]

    for possibility in tile_possibilities:
        if top_tile_info is not None:
            if not _match_top_bottom(top_tile_info[1], possibility):
                continue
        if left_tile_info is not None:
            if not _match_left_right(left_tile_info[1], possibility):
                continue
        return possibility
    return None


def _get_potential_next_tiles(
    left_tile_info, top_tile_info, potential_neighbors, placed_tile_ids
):
    if left_tile_info is not None and top_tile_info is not None:
        potentials = potential_neighbors[left_tile_info[0]].intersection(
            potential_neighbors[top_tile_info[0]]
        )
    elif left_tile_info is not None:
        potentials = potential_neighbors[left_tile_info[0]]
    elif top_tile_info is not None:
        potentials = potentials = potential_neighbors[top_tile_info[0]]

    return [p for p in potentials if p not in placed_tile_ids]


def _get_image_with_borders(puzzle_input):
    tiles = _parse_tiles(puzzle_input)
    potential_neighbors = _get_potential_neighbors(tiles)
    corner_tile_ids = _get_corner_tile_ids(potential_neighbors)

    # Let's place one of the corners, and start building out from there
    first_tile_id = corner_tile_ids[0]
    # Note: I'm going to "cheat" to so that I can visually follow the example
    # and set up this first tile so I know it matches the example
    first_tile = np.fliplr(tiles[first_tile_id])
    first_tile_neighbor_id_1, first_tile_neighbor_id_2 = potential_neighbors[
        first_tile_id
    ]
    while not (
        (
            _has_border(tile=tiles[first_tile_neighbor_id_1], border=first_tile[-1])
            and _has_border(
                tile=tiles[first_tile_neighbor_id_2], border=first_tile[:, -1]
            )
        )
        or (
            _has_border(tile=tiles[first_tile_neighbor_id_2], border=first_tile[-1])
            and _has_border(
                tile=tiles[first_tile_neighbor_id_1], border=first_tile[:, -1]
            )
        )
    ):
        # Rotate until these tiles can fit
        first_tile = np.rot90(first_tile)

    placed_tile_ids = {first_tile_id}
    image = {
        (0, 0): (first_tile_id, first_tile),
    }

    # The image is a square so we can determine the width & height
    image_width_and_height = int(math.sqrt(len(tiles)))

    for y in range(image_width_and_height):
        for x in range(image_width_and_height):
            if (x, y) == (0, 0):
                # We already placed this manually
                continue

            potential_ids_for_here = _get_potential_next_tiles(
                left_tile_info=image.get((x - 1, y)),
                top_tile_info=image.get((x, y - 1)),
                potential_neighbors=potential_neighbors,
                placed_tile_ids=placed_tile_ids,
            )
            for potential_tile_id in potential_ids_for_here:
                fitting_configuration = _find_fit(
                    tile=tiles[potential_tile_id],
                    left_tile_info=image.get((x - 1, y)),
                    top_tile_info=image.get((x, y - 1)),
                )
                if fitting_configuration is not None:
                    break

            if fitting_configuration is None:
                raise ValueError("Something went wrong.")
            image[(x, y)] = (potential_tile_id, fitting_configuration)
            placed_tile_ids.add(potential_tile_id)

    return {key: tile for key, (tile_id, tile) in image.items()}


def _remove_border(image_with_borders):
    image_dimension = max(x for x, y in image_with_borders.keys())
    image_rows = []
    for y in range(image_dimension + 1):
        image_row = image_with_borders[(0, y)][1:-1, 1:-1]
        for x in range(1, image_dimension + 1):
            image_row = np.concatenate(
                (image_row, image_with_borders[(x, y)][1:-1, 1:-1]), axis=1
            )
        image_rows.append(image_row)

    image = image_rows[0]
    for y in range(1, image_dimension + 1):
        image = np.concatenate((image, image_rows[y]), axis=0)
    return image


def _remove_sea_monsters(image):
    # The image might be rotated incorrectly.
    # We assume that only one position contains ~sea monsters~
    image_possibilities = [
        image,
        np.rot90(image),
        np.rot90(np.rot90(image)),
        np.rot90(np.rot90(np.rot90(image))),
        np.fliplr(image),
        np.rot90(np.fliplr(image)),
        np.rot90(np.rot90(np.fliplr(image))),
        np.rot90(np.rot90(np.rot90(np.fliplr(image)))),
    ]
    side_length, _ = image.shape

    # Let's  search for sea monsters!
    # Sea monsters look like this
    """
                  #
#    ##    ##    ###
 #  #  #  #  #  #
    """

    for image_position in image_possibilities:
        found_sea_monster = False
        for x in range(side_length - SEA_MONSTER_LENGTH + 1):
            for y in range(SEA_MONSTER_HEIGHT - 1, side_length):
                sea_monster_shape = (
                    (x, y - 1),
                    (x + 1, y),
                    (x + 4, y),
                    (x + 5, y - 1),
                    (x + 6, y - 1),
                    (x + 7, y),
                    (x + 10, y),
                    (x + 11, y - 1),
                    (x + 12, y - 1),
                    (x + 13, y),
                    (x + 16, y),
                    (x + 17, y - 1),
                    (x + 18, y - 1),
                    (x + 18, y - 2),
                    (x + 19, y - 1),
                )

                if all(
                    image_position[sm_y][sm_x] == "#"
                    for sm_x, sm_y in sea_monster_shape
                ):
                    # There be sea monster!!
                    found_sea_monster = True
                    for sm_x, sm_y in sea_monster_shape:
                        image_position[sm_y][sm_x] = "."
        if found_sea_monster:
            return image_position


def get_water_roughness(puzzle_input):
    image_with_borders = _get_image_with_borders(puzzle_input)
    image = _remove_border(image_with_borders)
    image_without_sea_monsters = _remove_sea_monsters(image)
    return np.sum(np.vectorize(lambda val: val == "#")(image_without_sea_monsters))


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_corner_ids_product(puzzle_input)}")
    print(f"Part 2: {get_water_roughness(puzzle_input)}")
