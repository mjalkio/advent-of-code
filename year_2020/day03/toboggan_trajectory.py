from pathlib import Path


def num_trees_hit(map, horizontal_change=1, vertical_change=1):
    return None


if __name__ == '__main__':
    puzzle_input_path = Path(Path(__file__).parent, 'puzzle_input.txt')
    with puzzle_input_path.open() as f:
        puzzle_input = f.read()

    print(f"Part 1: {num_trees_hit(puzzle_input)}")
