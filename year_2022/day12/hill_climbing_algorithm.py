import heapq
from collections import namedtuple

from util import read_puzzle_input

Node = namedtuple("Node", ["num_steps", "coords"])


def fewest_steps(puzzle_input):
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

    # Breadth-first search (BFS)
    queue = [Node(num_steps=0, coords=starting_pos)]
    visited = set()
    while len(queue) > 0:
        current_node = heapq.heappop(queue)
        if current_node.coords == best_signal_pos:
            return current_node.num_steps
        visited.add(current_node.coords)

        curr_x, curr_y = current_node.coords
        neighbors = [
            (curr_x + 1, curr_y),
            (curr_x - 1, curr_y),
            (curr_x, curr_y + 1),
            (curr_x, curr_y - 1),
        ]
        for (x, y) in neighbors:
            if (
                (x, y) not in heightmap
                or (x, y) in visited
                or heightmap[(x, y)] > heightmap[(curr_x, curr_y)] + 1
            ):
                continue
            heapq.heappush(
                queue,
                Node(
                    num_steps=current_node.num_steps + 1,
                    coords=(x, y),
                ),
            )


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {fewest_steps(puzzle_input)}")
    print(f"Part 2: {fewest_steps(puzzle_input)}")
