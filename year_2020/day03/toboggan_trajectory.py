from pathlib import Path

TREE = '#'


def num_trees_hit(tree_map, horizontal_change=1, vertical_change=1):
    tree_map_list = [line for line in tree_map.split() if line != '']
    tree_map_width = len(tree_map_list[0])
    vertical_location = 0
    horizontal_location = 0

    num_trees_hit = 0
    while vertical_location < len(tree_map_list):
        if tree_map_list[vertical_location][horizontal_location] == TREE:
            num_trees_hit += 1

        vertical_location += vertical_change
        horizontal_location = (horizontal_location + horizontal_change) % tree_map_width
    return num_trees_hit


def part_2(tree_map):
    product = 1
    slopes = (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    )

    for horizontal_change, vertical_change in slopes:
        product *= num_trees_hit(
            tree_map=tree_map,
            horizontal_change=horizontal_change,
            vertical_change=vertical_change,
        )

    return product


if __name__ == '__main__':
    puzzle_input_path = Path(Path(__file__).parent, 'puzzle_input.txt')
    with puzzle_input_path.open() as f:
        puzzle_input = f.read()

    print(f"Part 1: {num_trees_hit(tree_map=puzzle_input, horizontal_change=3, vertical_change=1)}")
    print(f"Part 2: {part_2(tree_map=puzzle_input)}")
