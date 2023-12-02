import heapq
import math
from collections import namedtuple

from util import read_puzzle_input

Node = namedtuple("Node", ["num_steps", "coords"])


def _parse_input(puzzle_input):
    lines = puzzle_input.split("\n")
    heightmap = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "S":
                # Current position
                starting_pos = (x, y)
                heightmap[(x, y)] = ord("a")
            elif lines[y][x] == "E":
                best_signal_pos = (x, y)
                heightmap[(x, y)] = ord("z")
            else:
                heightmap[(x, y)] = ord(lines[y][x])
    return heightmap, starting_pos, best_signal_pos


def _bfs(heightmap, starting_pos, best_signal_pos):
    # Breadth-first search (BFS)
    queue = [Node(num_steps=0, coords=starting_pos)]
    visited = set([starting_pos])
    while len(queue) > 0:
        current_node = heapq.heappop(queue)
        if current_node.coords == best_signal_pos:
            return current_node.num_steps

        curr_x, curr_y = current_node.coords
        neighbors = [
            (curr_x + 1, curr_y),
            (curr_x - 1, curr_y),
            (curr_x, curr_y + 1),
            (curr_x, curr_y - 1),
        ]
        for x, y in neighbors:
            if (
                (x, y) not in heightmap
                or (x, y) in visited
                or heightmap[(x, y)] > heightmap[(curr_x, curr_y)] + 1
            ):
                continue
            visited.add((x, y))
            heapq.heappush(
                queue,
                Node(
                    num_steps=current_node.num_steps + 1,
                    coords=(x, y),
                ),
            )
    return math.inf


def fewest_steps(puzzle_input):
    heightmap, starting_pos, best_signal_pos = _parse_input(puzzle_input)
    return _bfs(heightmap, starting_pos, best_signal_pos)


def fewest_steps_possible(puzzle_input):
    heightmap, _, best_signal_pos = _parse_input(puzzle_input)
    return min(
        [
            _bfs(heightmap, pos, best_signal_pos)
            for pos, height in heightmap.items()
            if height == ord("a")
        ]
    )


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {fewest_steps(puzzle_input)}")
    print(f"Part 2: {fewest_steps_possible(puzzle_input)}")
