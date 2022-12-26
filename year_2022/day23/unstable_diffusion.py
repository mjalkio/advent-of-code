from util import read_puzzle_input

N = "north"
S = "south"
W = "west"
E = "east"

DIRECTION_ORDER = [N, S, W, E]


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


def _plan(elf, elves, round_num):
    return None


def num_empty_ground_tiles(puzzle_input, num_rounds=10):
    elves = set()
    for y, line in enumerate(puzzle_input.strip().split("\n")):
        for x in range(len(line)):
            if line[x] == "#":
                elves.add((x, -y))

    for round_num in range(num_rounds):
        planned_moves = {}
        for elf in elves:
            if _has_adjacent(elf=elf, elves=elves):
                planned_moves[elf] = _plan(elf, elves, round_num)
    return 0


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {num_empty_ground_tiles(puzzle_input)}")
    print(f"Part 2: {num_empty_ground_tiles(puzzle_input)}")
