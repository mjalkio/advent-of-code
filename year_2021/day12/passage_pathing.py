from copy import copy
from collections import defaultdict

from util import read_puzzle_input


START = "start"
END = "end"


def _is_big_cave(cave):
    return cave.isupper()


def get_num_paths(puzzle_input, max_small_cave_visits=1):
    edges = [line.split("-") for line in puzzle_input.split("\n")]
    outbound_edges = defaultdict(list)
    for x, y in edges:
        outbound_edges[x].append(y)
        outbound_edges[y].append(x)

    potential_paths = [[START]]
    num_paths = 0
    while len(potential_paths) > 0:
        current_path = potential_paths.pop()
        current_cave = current_path[-1]
        if current_cave == END:
            num_paths += 1
            continue

        for next_cave in outbound_edges[current_cave]:
            if _is_big_cave(next_cave) or next_cave not in current_path:
                new_path = copy(current_path)
                new_path.append(next_cave)
                potential_paths.append(new_path)

    return num_paths


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_num_paths(puzzle_input)}")
    print(f"Part 2: {get_num_paths(puzzle_input, max_small_cave_visits=2)}")
