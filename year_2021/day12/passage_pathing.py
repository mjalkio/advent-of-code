from copy import copy
from collections import defaultdict, namedtuple

from util import read_puzzle_input


START = "start"
END = "end"

Path = namedtuple("Path", ["current_cave", "visited_caves", "has_revisited_small_cave"])


def _is_big_cave(cave):
    return cave.isupper()


def get_num_paths(puzzle_input, can_revisit_single_small_cave=False):
    edges = [line.split("-") for line in puzzle_input.split("\n")]
    outbound_edges = defaultdict(list)
    for x, y in edges:
        outbound_edges[x].append(y)
        outbound_edges[y].append(x)

    potential_paths = [
        Path(
            current_cave=START,
            visited_caves=set([START]),
            has_revisited_small_cave=False,
        )
    ]
    num_paths = 0
    while len(potential_paths) > 0:
        current_cave, visited_caves, has_revisited_small_cave = potential_paths.pop()
        if current_cave == END:
            num_paths += 1
            continue

        for next_cave in outbound_edges[current_cave]:
            if _is_big_cave(next_cave) or next_cave not in visited_caves:
                is_small_cave_revisit = False
            elif (
                can_revisit_single_small_cave
                and not _is_big_cave(next_cave)
                and next_cave != START
                and not has_revisited_small_cave
            ):
                is_small_cave_revisit = True
            else:
                continue

            new_visited_caves = copy(visited_caves)
            new_visited_caves.add(next_cave)
            potential_paths.append(
                Path(
                    current_cave=next_cave,
                    visited_caves=new_visited_caves,
                    has_revisited_small_cave=has_revisited_small_cave
                    or is_small_cave_revisit,
                )
            )

    return num_paths


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_num_paths(puzzle_input)}")
    print(f"Part 2: {get_num_paths(puzzle_input, can_revisit_single_small_cave=True)}")
