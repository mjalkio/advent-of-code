from collections import Counter

from util import read_puzzle_input

N = "north"
S = "south"
W = "west"
E = "east"

DIRECTION_ORDER = [N, S, W, E]

DIRECTION_VECTORS = {
    N: (0, 1),
    S: (0, -1),
    W: (-1, 0),
    E: (1, 0),
}

ADJACENCY_CHECKS = {
    N: [(0, 1), (1, 1), (-1, 1)],
    S: [(0, -1), (1, -1), (-1, -1)],
    W: [(-1, 0), (-1, 1), (-1, -1)],
    E: [(1, 0), (1, 1), (1, -1)],
}


def _has_adjacent(elf, elves):
    x, y = elf
    adjacent_positions = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
        (x + 1, y + 1),
        (x - 1, y - 1),
        (x + 1, y - 1),
        (x - 1, y + 1),
    ]
    return any((x_adj, y_adj) in elves for x_adj, y_adj in adjacent_positions)


def _plan(elf, elves, directions):
    x, y = elf
    for direction in directions:
        if all(
            (x + adj_x, y + adj_y) not in elves
            for adj_x, adj_y in ADJACENCY_CHECKS[direction]
        ):
            dir_x, dir_y = DIRECTION_VECTORS[direction]
            return (x + dir_x, y + dir_y)
    return None


def num_empty_ground_tiles(puzzle_input, num_rounds=10):
    elves = set()
    for y, line in enumerate(puzzle_input.strip().split("\n")):
        for x in range(len(line)):
            if line[x] == "#":
                elves.add((x, -y))

    for round_num in range(num_rounds):
        directions = (
            DIRECTION_ORDER[round_num % len(DIRECTION_ORDER) :]
            + DIRECTION_ORDER[: round_num % len(DIRECTION_ORDER)]
        )
        proposed_moves = {}
        for elf in elves:
            if _has_adjacent(elf=elf, elves=elves):
                proposal = _plan(elf, elves, directions)
                if proposal is not None:
                    proposed_moves[elf] = proposal
        proposal_counts = Counter(proposed_moves.values())

        new_elves = set()
        for elf in elves:
            if elf in proposed_moves and proposal_counts[proposed_moves[elf]] == 1:
                new_elves.add(proposed_moves[elf])
            else:
                new_elves.add(elf)
        elves = new_elves
    return 0


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {num_empty_ground_tiles(puzzle_input)}")
    print(f"Part 2: {num_empty_ground_tiles(puzzle_input)}")
