from util import read_puzzle_input

DIRECTION_MAP = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1),
}


def _is_touching(head_x, head_y, tail_x, tail_y):
    return abs(head_x - tail_x) <= 1 and abs(head_y - tail_y) <= 1


def num_positions_tail_visits(puzzle_input):
    steps = []
    for line in puzzle_input.split("\n"):
        if line == "":
            continue
        direction, num_steps = line.split()
        steps += [DIRECTION_MAP[direction]] * int(num_steps)

    head_x = 0
    head_y = 0
    tail_x = 0
    tail_y = 0
    tail_positions = set([(tail_x, tail_y)])
    for dx, dy in steps:
        head_x += dx
        head_y += dy

        if _is_touching(head_x, head_y, tail_x, tail_y):
            continue

        if head_x > tail_x:
            tail_x += 1
        elif head_x < tail_x:
            tail_x -= 1

        if head_y > tail_y:
            tail_y += 1
        elif head_y < tail_y:
            tail_y -= 1

        tail_positions.add((tail_x, tail_y))
    return len(tail_positions)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {num_positions_tail_visits(puzzle_input)}")
    print(f"Part 2: {num_positions_tail_visits(puzzle_input)}")
